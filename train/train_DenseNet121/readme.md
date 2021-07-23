
## DenseNet121

실제로 체감상으로도 학습 속도가 조금 빠른 것 같긴 했다. 

### Train Results


### Evaluation Results

|  | 3dpw | lsp | mpi-inf-3dhp | 
|:--:|:--:|:--:|:--:|
| MPJPE | 273.95 | | 287.97 |
| Reconstruction Error | 127.44 | | 142.93 |

### Train Options

```
train = self.parser.add_argument_group('Training Options')
train.add_argument('--num_epochs', type=int, default=50, help='Total number of training epochs')
train.add_argument("--lr", type=float, default=5e-5, help="Learning rate")
train.add_argument('--batch_size', type=int, default=100, help='Batch size')
train.add_argument('--summary_steps', type=int, default=50, help='Summary saving frequency')
train.add_argument('--test_steps', type=int, default=1000, help='Testing frequency during training')
train.add_argument('--checkpoint_steps', type=int, default=10000, help='Checkpoint saving frequency')
train.add_argument('--img_res', type=int, default=224, help='Rescale bounding boxes to size [img_res, img_res] before feeding them in the network') 
train.add_argument('--rot_factor', type=float, default=30, help='Random rotation in the range [-rot_factor, rot_factor]') 
train.add_argument('--noise_factor', type=float, default=0.4, help='Randomly multiply pixel values with factor in the range [1-noise_factor, 1+noise_factor]') 
train.add_argument('--scale_factor', type=float, default=0.25, help='Rescale bounding boxes by a factor of [1-scale_factor,1+scale_factor]') 
train.add_argument('--ignore_3d', default=False, action='store_true', help='Ignore GT 3D data (for unpaired experiments') 
train.add_argument('--shape_loss_weight', default=0, type=float, help='Weight of per-vertex loss') 
train.add_argument('--keypoint_loss_weight', default=5., type=float, help='Weight of 2D and 3D keypoint loss') 
train.add_argument('--pose_loss_weight', default=1., type=float, help='Weight of SMPL pose loss') 
train.add_argument('--beta_loss_weight', default=0.001, type=float, help='Weight of SMPL betas loss') 
train.add_argument('--openpose_train_weight', default=0., help='Weight for OpenPose keypoints during training') 
train.add_argument('--gt_train_weight', default=1., help='Weight for GT keypoints during training') 
train.add_argument('--run_smplify', default=False, action='store_true', help='Run SMPLify during training') 
train.add_argument('--smplify_threshold', type=float, default=100., help='Threshold for ignoring SMPLify fits during training') 
train.add_argument('--num_smplify_iters', default=100, type=int, help='Number of SMPLify iterations') 

```
