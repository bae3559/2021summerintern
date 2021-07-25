### Parameters

22410245

### Loss( it is not the result of DenseNet201 )
| loss | loss_pose | loss_betas | loss_keypoints | loss_shape |
|:---:|:---:|:---:|:---:|:---:|
|<img src="https://user-images.githubusercontent.com/42258047/126899643-024f26b8-f41f-43d9-b464-90d7c7c9c7d9.png" width="300"> | <img src="https://user-images.githubusercontent.com/42258047/126899658-6a19c453-095f-4009-bd08-340ed1726677.png" width="300"> | <img src="https://user-images.githubusercontent.com/42258047/126899680-d3a45fac-53c3-4b6b-93fe-677175516c04.png" width="300"> | <img src="https://user-images.githubusercontent.com/42258047/126899699-58449707-01ea-427a-b6a3-0d8b530cfb72.png" width="300"> | <img src="https://user-images.githubusercontent.com/42258047/126899734-b872b51b-f43d-4cb0-a9ee-cc50a64cf850.png" width="300">| 


### Evaluation Results

|  | 3dpw | mpi-inf-3dhp | h36m-p1 | h36m-p2 |
|:--:|:--:|:--:|:--:|:--:|
| MPJPE | 133.7542 | 115.5370 | 137.7607 | 152.2707 |
| Reconstruction Error | 74.77 | 76.7496 | 77.0025 | 77.4746 | 


| | lsp | 
|:--:|:--:|
| Accuracy | 0.9001 |
| F1 | 0.8379 |
| Parts Accuracy | 0.87318 |
| Parts F1 (BG) | 0.6063 | 


### Final Results
![image](https://user-images.githubusercontent.com/42258047/126900317-f26588c0-287a-452d-aa01-723cf7261e6e.png) ![image](https://user-images.githubusercontent.com/42258047/126900333-b1b5576c-c625-4c18-ab7a-e322921db8ef.png)

![image](https://user-images.githubusercontent.com/42258047/126900339-5b12cccb-57bc-4842-8aff-17a68031ac88.png) ![image](https://user-images.githubusercontent.com/42258047/126900346-5cc6e1d4-7e31-4f9c-800c-6195f6ebcb3a.png)

![image](https://user-images.githubusercontent.com/42258047/126900380-dd988978-205e-4895-a3af-55959d1b1c81.png) ![image](https://user-images.githubusercontent.com/42258047/126900389-6d54ca9f-af2b-443b-9e0b-56a7f6a37f5a.png)

![image](https://user-images.githubusercontent.com/42258047/126900408-c5cad757-3e9f-4cfb-ab32-46d951abfdca.png)




### Failure Case

![image](https://user-images.githubusercontent.com/42258047/126900414-c515b167-ed9c-41de-8a32-10ffaf755dd9.png) ![image](https://user-images.githubusercontent.com/42258047/126900417-59c2e702-15c7-44de-bb60-9c920cbff0ed.png)

![image](https://user-images.githubusercontent.com/42258047/126900425-a356b539-5a1b-4e89-ba95-a4111daab751.png) ![image](https://user-images.githubusercontent.com/42258047/126900439-4ba333f7-6041-478e-971e-e626db670385.png)

![image](https://user-images.githubusercontent.com/42258047/126900447-342cbc5a-ec4e-4800-817a-9f8bc039dc11.png)


### train options

There is issue with 'load the pretrained DenseNet201' because of the 'CUDA out of memory'.

So, I changed the batch_size to 45 from 50. 

```
train = self.parser.add_argument_group('Training Options')
train.add_argument('--num_epochs', type=int, default=50, help='Total number of training epochs')
train.add_argument("--lr", type=float, default=5e-5, help="Learning rate")
train.add_argument('--batch_size', type=int, default=45, help='Batch size')
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
