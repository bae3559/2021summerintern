#20210726 train_MobileNetV2 version
#whole model is same with HMR except discriminator part 
#this version doesn't include the discriminator . only include mobilenetv2+regression(3iter) part!
import torch
import torch.nn as nn
import numpy as np
import math
from utils.geometry import rot6d_to_rotmat
import torch.nn.utils.prune as prune
#from torchsummary import summary
from torchvision.models.utils import load_state_dict_from_url

model_urls = {
    'mobilenet_v2': 'https://download.pytorch.org/models/mobilenet_v2-b0353104.pth',
}

def count_parameters(model):
  return sum(p.numel() for p in model.parameters() if p.requires_grad)




def _make_divisible(v, divisor, min_value=None):
    """
    This function is taken from the original tf repo.
    It ensures that all layers have a channel number that is divisible by 8
    It can be seen here:
    https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/mobilenet.py
    :param v:
    :param divisor:
    :param min_value:
    :return:
    """
    if min_value is None:
        min_value = divisor
    new_v = max(min_value, int(v + divisor / 2) // divisor * divisor)
    # Make sure that round down does not go down by more than 10%.
    if new_v < 0.9 * v:
        new_v += divisor
    return new_v


class ConvBNReLU(nn.Sequential):
    def __init__(self, in_planes, out_planes, kernel_size=3, stride=1, groups=1, norm_layer=None):
        padding = (kernel_size - 1) // 2
        if norm_layer is None:
            norm_layer = nn.BatchNorm2d
        super(ConvBNReLU, self).__init__(
            nn.Conv2d(in_planes, out_planes, kernel_size, stride, padding, groups=groups, bias=False),
            norm_layer(out_planes),
            nn.ReLU6(inplace=True)
        )


class InvertedResidual(nn.Module):
    def __init__(self, inp, oup, stride, expand_ratio, norm_layer=None):
        super(InvertedResidual, self).__init__()
        self.stride = stride
        assert stride in [1, 2]

        if norm_layer is None:
            norm_layer = nn.BatchNorm2d

        hidden_dim = int(round(inp * expand_ratio))
        self.use_res_connect = self.stride == 1 and inp == oup

        layers = []
        if expand_ratio != 1:
            # pw
            layers.append(ConvBNReLU(inp, hidden_dim, kernel_size=1, norm_layer=norm_layer))
        layers.extend([
            # dw
            ConvBNReLU(hidden_dim, hidden_dim, stride=stride, groups=hidden_dim, norm_layer=norm_layer),
            # pw-linear
            nn.Conv2d(hidden_dim, oup, 1, 1, 0, bias=False),
            norm_layer(oup),
        ])
        self.conv = nn.Sequential(*layers)

    def forward(self, x):
        if self.use_res_connect:
            return x + self.conv(x)
        else:
            return self.conv(x)

class MY_MODEL(nn.Module):
    
    def __init__(self,smpl_init_param, width_mult=1.0,
                 inverted_residual_setting=None,
                 round_nearest=8,
                 block=None,
                 norm_layer=None):
                 
        npose = 24*6
        
        super(MY_MODEL, self).__init__()
        
        if block is None:
            block = InvertedResidual

        if norm_layer is None:
            norm_layer = nn.BatchNorm2d

        input_channel = 32
        last_channel = 1280
        num_classes = 1000
        if inverted_residual_setting is None:
            inverted_residual_setting = [
                # t, c, n, s
                [1, 16, 1, 1],
                [6, 24, 2, 2],
                [6, 32, 3, 2],
                [6, 64, 4, 2],
                [6, 96, 3, 1],
                [6, 160, 3, 2],
                [6, 320, 1, 1],
            ]

        # only check the first element, assuming user knows t,c,n,s are required
        if len(inverted_residual_setting) == 0 or len(inverted_residual_setting[0]) != 4:
            raise ValueError("inverted_residual_setting should be non-empty "
                             "or a 4-element list, got {}".format(inverted_residual_setting))

        # building first layer
        input_channel = _make_divisible(input_channel * width_mult, round_nearest)
        self.last_channel = _make_divisible(last_channel * max(1.0, width_mult), round_nearest)
        features = [ConvBNReLU(3, input_channel, stride=2, norm_layer=norm_layer)]
        # building inverted residual blocks
        for t, c, n, s in inverted_residual_setting:
            output_channel = _make_divisible(c * width_mult, round_nearest)
            for i in range(n):
                stride = s if i == 0 else 1
                features.append(block(input_channel, output_channel, stride, expand_ratio=t, norm_layer=norm_layer))
                input_channel = output_channel
        # building last several layers
        features.append(ConvBNReLU(input_channel, self.last_channel, kernel_size=1, norm_layer=norm_layer))
        # make it nn.Sequential
        self.features = nn.Sequential(*features)

        # building classifier
        #self.classifier = nn.Sequential(
        #    nn.Dropout(0.2),
        #    nn.Linear(self.last_channel, num_classes),
        #)

        #self.conv = nn.Conv2d(self.last_channel, 24, 1, 1, 0, bias=False)

        self.classifier2 = nn.Linear(1176,24)
        self.classifier1 = nn.Linear(1280,24)
        
        self.conv2 = nn.Conv2d(self.last_channel, 24, 1, 1, 0, bias=False)
        self.soft = nn.Softmax(dim=1)
        
        self.conv3 = nn.Linear(24*24, 1024)
        
        self.decpose2 = nn.Linear(1024+npose+13, npose)
        self.decshape2 = nn.Linear(1024+npose+13, 10)
        self.deccam2 = nn.Linear(1024+npose+13, 3)
        
        self.poseconv = nn.Linear(npose+npose, npose)
        self.shapeconv = nn.Linear(20, 10)
        self.camconv = nn.Linear(6,3)
        
        self.avgpool = nn.AdaptiveAvgPool2d((1, 1))
        
        # weight initialization
        for m in self.modules():
            if isinstance(m, nn.Conv2d):
                nn.init.kaiming_normal_(m.weight, mode='fan_out')
                if m.bias is not None:
                    nn.init.zeros_(m.bias)
            elif isinstance(m, (nn.BatchNorm2d, nn.GroupNorm)):
                nn.init.ones_(m.weight)
                nn.init.zeros_(m.bias)
            elif isinstance(m, nn.Linear):
                nn.init.normal_(m.weight, 0, 0.01)
                nn.init.zeros_(m.bias)
        
        nn.init.xavier_uniform_(self.decpose2.weight, gain=0.01)
        nn.init.xavier_uniform_(self.decshape2.weight, gain=0.01)
        nn.init.xavier_uniform_(self.deccam2.weight, gain=0.01)
        
        
        mean_params = np.load(smpl_init_param)
        init_pose = torch.from_numpy(mean_params['pose'][:]).unsqueeze(0)
        init_shape = torch.from_numpy(mean_params['shape'][:].astype('float32')).unsqueeze(0)
        init_cam = torch.from_numpy(mean_params['cam']).unsqueeze(0)
        self.register_buffer('init_pose', init_pose)
        self.register_buffer('init_shape', init_shape)
        self.register_buffer('init_cam', init_cam)

        
    def _forward_impl(self, x):
        # This exists since TorchScript doesn't support inheritance, so the superclass method
        # (this one) needs to have a name other than `forward` that can be accessed in a subclass
        x = self.features(x)
        # Cannot use "squeeze" as batch-size can be 1 => must use reshape with x.shape[0]
        #x = nn.functional.adaptive_avg_pool2d(x, 1)
        #x = self.classifier(x)
        return x
        

    def forward(self, x, init_pose = None, init_shape = None, init_cam=None, n_iter=3):

        
        batch_size = x.shape[0]
        
        if init_pose is None:
            init_pose = self.init_pose.expand(batch_size, -1)
        if init_shape is None:
            init_shape = self.init_shape.expand(batch_size, -1)
        if init_cam is None:
            init_cam = self.init_cam.expand(batch_size, -1)
        
        x = self._forward_impl(x)       # outsize 64,1280,7,7
        
        #print(x.shape)
        
        #x = self.conv(x)

                
        x2 = self.conv2(x) 
        x2 = x2.view(x2.size(0),-1)
        
        #print(x2.shape)
        x2 = self.classifier2(x2)
        x2 = self.soft(x2)
        
        
        x = self.avgpool(x)
        x = x.view(x.size(0), -1)
        #print(x.shape)
        x = self.classifier1(x)       
        
        x = torch.reshape(x, [batch_size, 1,24])
        x2 = torch.reshape(x2, [batch_size, 24,1])
        
        
        x = torch.matmul(x2, x)
        
        #### regression ####
        xv = x.view(x.size(0),-1)
        xv = x.view(x.size(0),-1)
        
        pred_pose = init_pose
        pred_shape = init_shape
        pred_cam = init_cam
        
        xv = self.conv3(xv)
        
        for i in range(n_iter):
 
 
            xc = torch.cat([xv,pred_pose, pred_shape, pred_cam],1)
            #pose1 = torch.cat((self.decpose(xc), pred_pose),1)
            pose = torch.cat((self.decpose2(xc), pred_pose), 1)
            shape = torch.cat((self.decshape2(xc), pred_shape), 1)
            cam = torch.cat((self.deccam2(xc),pred_cam), 1)
            
            pred_pose = self.poseconv(pose)
            pred_shpe = self.shapeconv(shape)
            pred_cam = self.camconv(cam)
        
        pred_rotmat = rot6d_to_rotmat(pred_pose).view(batch_size, 24, 3, 3)
        
        return pred_rotmat, pred_shape, pred_cam

def my_model(smpl_mean_params, pretrained=True, **kwargs):

    model = MY_MODEL(smpl_mean_params)
    

    if pretrained:
        #state_dict = load_state_dict_from_url(model_urls['mobilenet_v2'], progress=True)
        #model.load_state_dict(state_dict,strict=False)
        checkpoint = torch.load('logs/train_MobileNetV2/checkpoints/2021_07_28-16_27_22.pt')
        model.load_state_dict(checkpoint['model'], strict=False)
    print(count_parameters(model))
    
    #summary(model, (3,224,224))
    return model


