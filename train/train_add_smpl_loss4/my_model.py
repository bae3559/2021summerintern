import torch
import torch.nn as nn
import torchvision.models.resnet as resnet
import numpy as np
import math
from utils.geometry import rot6d_to_rotmat

def conv3x3(in_planes, out_planes, stride=1):
    """3x3 convolution with padding"""
    return nn.Conv2d(in_planes, out_planes, kernel_size=3, stride=stride,
                     padding=1, bias=False)


def conv1x1(in_planes, out_planes, stride=1):
    """1x1 convolution"""
    return nn.Conv2d(in_planes, out_planes, kernel_size=1, stride=stride, bias=False)

class Bottleneck(nn.Module):

    expansion = 4
    def __init__(self, inplanes, planes, stride=1, downsample=None):
      super(Bottleneck, self).__init__()
      
      self.conv1 = conv1x1(inplanes, planes)
      self.bn1 = nn.BatchNorm2d(planes)
      self.conv2 = conv3x3(planes, planes,stride)
      self.bn2 = nn.BatchNorm2d(planes)
      self.conv3 = conv1x1(planes, planes * self.expansion)
      self.bn3 = nn.BatchNorm2d(planes * self.expansion)

      self.downsample = downsample
      self.relu = nn.ReLU(inplace=True)
      self.stride = stride

    def forward(self, x):

      identity = x

      out = self.conv1(x)
      out = self.bn1(out)
      out = self.relu(out)

      out = self.conv2(out)
      out = self.bn2(out)
      out = self.relu(out)

      out = self.conv3(out)
      out = self.bn3(out)
      
      if self.downsample != None:
        identity = self.downsample(x)

      out += identity 
      out = self.relu(out)

      return out


class MY_MODEL(nn.Module):
    """
    Implement this module with your own idea

    """
    
    def __init__(self, block, layers, smpl_init_param):
        """
        #example code
        self.conv1 = nn.Conv2d(3, 64, kernel_size=7, stride=2, padding=3, bias=False)
        self.bn1 = nn.BatchNorm2d(64)
        self.relu = nn.ReLU(inplace=True) 
        self.maxpool = nn.MaxPool2d(kernel_size=3, stride=2, padding=1)

        """
        npose = 24*6
        
        super(MY_MODEL, self).__init__()
        self.inplanes = 64

        #inputs = 3x224x224
        self.conv1 = nn.Conv2d(3, 64, kernel_size=7, stride=2, padding=3, bias=False) 
        # outputs = self.conv1(inputs)라면, outputs.shape = [64x112x112]
        self.bn1 = nn.BatchNorm2d(64)
        self.relu = nn.ReLU(inplace=True)
        self.maxpool = nn.MaxPool2d(kernel_size=3, stride=2, padding=1)
        #  64x56x56 
        #========================================================================
        # layers = [3,4,6,3] : resnet50
        self.layer1 = self._make_layer(block, 64, layers[0])
        self.layer2 = self._make_layer(block, 128, layers[1], stride=2)
        self.layer3 = self._make_layer(block, 256, layers[2], stride=2)
        self.layer4 = self._make_layer(block, 512, layers[3], stride=2)
        #========================================================================
        
        self.avgpool = nn.AvgPool2d(7, stride=1)
        self.fc1 = nn.Linear(512 * block.expansion+npose+13, 1024)
        self.drop1 = nn.Dropout()
        
        self.fc2 = nn.Linear(1024,1024)
        self.drop2 = nn.Dropout()
        
        self.decpose = nn.Linear(1024, npose)
        self.decshape = nn.Linear(1024, 10)
        self.deccam = nn.Linear(1024, 3)
        
        nn.init.xavier_uniform_(self.decpose.weight, gain=0.01)
        nn.init.xavier_uniform_(self.decshape.weight, gain=0.01)
        nn.init.xavier_uniform_(self.deccam.weight, gain=0.01)
        
        # weight 초기화 
        for m in self.modules():
          if isinstance(m, nn.Conv2d):
            nn.init.kaiming_normal_(m.weight, mode='fan_out', nonlinearity='relu')
          elif isinstance(m, nn.BatchNorm2d):
            nn.init.constant_(m.weight,1)
            nn.init.constant_(m.bias,1)
            
            
        mean_params = np.load(smpl_init_param)
        init_pose = torch.from_numpy(mean_params['pose'][:]).unsqueeze(0)
        init_shape = torch.from_numpy(mean_params['shape'][:].astype('float32')).unsqueeze(0)
        init_cam = torch.from_numpy(mean_params['cam']).unsqueeze(0)
        self.register_buffer('init_pose', init_pose)
        self.register_buffer('init_shape', init_shape)
        self.register_buffer('init_cam', init_cam)


    def _make_layer(self, block, planes, blocks, stride=1):
        downsample = None
        # downsample의 경우 stride가 2일 때, feature size가 줄어드니까, identity꺼도 낮춰주려고 사용하는 건데, 여기서는 더불어서 channel size 맞춰주는 용도로도 쓴다! 
        # 뭐 결국 크기가 안 맞으면 크기가 맞게 바꿔 주는 거 
        if stride != 1 or self.inplanes != planes * block.expansion: # self.inplanes = 64 != 64*4 = 256 
          downsample = nn.Sequential( conv1x1(self.inplanes, planes*block.expansion, stride), nn.BatchNorm2d(planes*block.expansion) ) # batchnorm2d (256)
              # batchnorm2d(512)
          layers=[]
          layers.append(block(self.inplanes, planes, stride, downsample)) 
          # Bottleneck(64, 64, 1, downsample)
          # Bottleneck(256,128,2, downsample(conv1x1(256,512,2)))
          self.inplanes = planes*block.expansion # 위에서 이제 크기를 맞춰 줬으니 inplanes도 256으로 업데이트 ! 
          # 이제 self.inplanes = 512
          for _ in range(1, blocks):
          # for _ in range(1, 3) sequential이 2개 더 append 되는거! 그래서 총 3개!
          # for _ in range(1, 4) sequential이 3개 더 append 
            layers.append(block(self.inplanes, planes))
    
          # self.layer1 = [ Bottleneck(64, 64, 1, downsample)
          #                 Bottleneck(256,64)
          #                 Bottleneck(256,64)]
          # self.layer2 = [Bottleneck(256,128,2, downsample)
          #                 Bottleneck(512,128)
          #                 Bottleneck(512,128)
          #                 Bottleneck(512,128)]
          return nn.Sequential(*layers)


    def forward(self, x, init_pose = None, init_shape = None, init_cam=None, n_iter=3):
        """
        #example code
        x = self.conv1(x)
        x = self.bn1(x)
        x = self.relu(x)
        x = self.maxpool(x)
 
        """
        
        batch_size = x.shape[0]
        
        if init_pose is None:
            init_pose = self.init_pose.expand(batch_size, -1)
        if init_shape is None:
            init_shape = self.init_shape.expand(batch_size, -1)
        if init_cam is None:
            init_cam = self.init_cam.expand(batch_size, -1)
        
        x = self.conv1(x)
        x = self.bn1(x)
        x = self.relu(x)
        x = self.maxpool(x)
        
        x1 = self.layer1(x)
        x2 = self.layer2(x1)
        x3 = self.layer3(x2)
        x4 = self.layer4(x3)
        
        xv = self.avgpool(x4)
        xv = xv.view(xv.size(0),-1)
        
        pred_pose = init_pose
        pred_shape = init_shape
        pred_cam = init_cam
        
        for i in range(n_iter):
 
            xc = torch.cat([xv,pred_pose, pred_shape, pred_cam],1)
            xc = self.fc1(xc)
            xc = self.drop1(xc)
            xc = self.fc2(xc)
            xc = self.drop2(xc)
            
        
            pred_pose = self.decpose(xc)+pred_pose
            pred_shpe = self.decshape(xc)+pred_shape
            pred_cam = self.deccam(xc)+pred_cam
        
        pred_rotmat = rot6d_to_rotmat(pred_pose).view(batch_size, 24, 3, 3)
        
        return pred_rotmat, pred_shape, pred_cam

def my_model(smpl_mean_params, pretrained=True, **kwargs):
    GPU_NUM = 2
    device = torch.device(f'cuda:{GPU_NUM}' if torch.cuda.is_available() else 'cpu')
    model = MY_MODEL(Bottleneck, [3,4,6,3], smpl_mean_params).to(device)

    if pretrained:
        resnet_imagenet = resnet.resnet50(pretrained=True)
        model.load_state_dict(resnet_imagenet.state_dict(),strict=False)
    return model

