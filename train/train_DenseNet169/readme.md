## Parameters

16,545,797

### Final Results
![image](https://user-images.githubusercontent.com/42258047/126870906-aac61228-5487-4cee-bb26-ebffdbede91f.png) ![image](https://user-images.githubusercontent.com/42258047/126870947-259cecf1-2b20-47f1-a6c3-677923d03e65.png) 
![image](https://user-images.githubusercontent.com/42258047/126871008-69b7730d-019c-4b9d-95ed-70b060994c91.png) ![image](https://user-images.githubusercontent.com/42258047/126871021-5d6206da-898f-477c-9f49-c36b0be54f4b.png)
![image](https://user-images.githubusercontent.com/42258047/126871094-ffd494b2-0816-4a9e-9e96-f909ca038bc7.png) ![image](https://user-images.githubusercontent.com/42258047/126871101-4813ef2a-e2ff-497a-a643-3c037b9d5452.png)




### Loss
| loss | loss_pose | loss_betas | loss_keypoints | loss_shape |
|:---:|:---:|:---:|:---:|:---:|
|<img src="https://user-images.githubusercontent.com/42258047/126870107-ab7acda3-2505-43d3-b029-c6cf5a65a286.png" width="300"> | <img src="https://user-images.githubusercontent.com/42258047/126870133-b5afb29d-9d13-4af7-92ea-72758369802f.png" width="300"> | <img src="https://user-images.githubusercontent.com/42258047/126870124-7056e062-819f-4b5b-80ef-1d5bc1e5a913.png" width="300"> | <img src="https://user-images.githubusercontent.com/42258047/126870113-313d1c15-6a62-4007-a39c-b1a036c75178.png" width="300"> | <img src="https://user-images.githubusercontent.com/42258047/126870148-94dbfcb9-8dff-4c9c-a47e-63b321a43ba8.png" width="300">| 


### Evaluation Results

|  | 3dpw | mpi-inf-3dhp | h36m-p1 | h36m-p2 |
|:--:|:--:|:--:|:--:|:--:|
| MPJPE | 121.13 | 112.89 | 131.1224 | 137.848 |
| Reconstruction Error | 71.37 | 76.54 | 77.22 | 76.174 | 


| | lsp | 
|:--:|:--:|
| Accuracy | 0.899 |
| F1 | 0.8369 |
| Parts Accuracy | 0.8716 |
| Parts F1 (BG) | 0.6065 | 


### Failure Case
![image](https://user-images.githubusercontent.com/42258047/126871079-3f416eff-b9b5-4aa1-945d-16df3f6697ec.png)
![image](https://user-images.githubusercontent.com/42258047/126871115-de61038d-dcb5-4711-9675-dfb016892203.png)
![image](https://user-images.githubusercontent.com/42258047/126871126-38b19d15-6e49-4fea-b221-91004236b54d.png)
![image](https://user-images.githubusercontent.com/42258047/126871129-6c76fbfa-9267-466a-ac7f-7dc81a198d82.png)


### train options

```
train = self.parser.add_argument_group('Training Options')
train.add_argument('--num_epochs', type=int, default=50, help='Total number of training epochs')
train.add_argument("--lr", type=float, default=5e-5, help="Learning rate")
train.add_argument('--batch_size', type=int, default=50, help='Batch size')
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
