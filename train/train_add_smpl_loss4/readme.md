## train results

## At 3 epoch

3 epoch째 인데도 불구하고 이전 결과들과 다르게 틀이 잡혀있음을 알 수 있다. 
또한 beta랑 pose가 다 잘 업데이트 되고 있음을 알 수 있다!

![3epoch](https://user-images.githubusercontent.com/42258047/126360625-3a9bf55e-124d-43d3-8b8e-d74639e1e05f.png) ![3epoch_2](https://user-images.githubusercontent.com/42258047/126360917-d20fc627-4719-41b7-b9e6-83e11f33b685.png)

loss 들도 다 생각보다 더 괜찮은 양상을 보여주고 있다! 내일이 되어야 전체 결과를 알 수 있겠지만! 

| loss | loss_pose | loss_betas | loss_keypoints | loss_shape |
|:---:|:---:|:---:|:---:|:---:|
|<img src="https://user-images.githubusercontent.com/42258047/126361507-0a65f9db-07a1-42ec-be8a-a06c76d090d8.png" width="250"> |<img src="https://user-images.githubusercontent.com/42258047/126361513-03fe52e9-add6-4774-b0eb-a1371f67f22b.png" width="250">| <img src="https://user-images.githubusercontent.com/42258047/126361516-233ecc8a-0e6c-4594-b3ef-0ad8daba07b3.png" width="250">  | <img src="https://user-images.githubusercontent.com/42258047/126361520-380ca33f-07f0-49a9-9ec0-2b68050d1eb8.png" width="250"> |<img src="https://user-images.githubusercontent.com/42258047/126362319-82363e55-7095-4967-bd44-30b6c8bcb7da.png" width="250"> | 

## At 20 epoch 



## Final Results
![image](https://user-images.githubusercontent.com/42258047/126597257-4f94e2f4-9668-41c2-8523-647d9ac8972a.png)

![image](https://user-images.githubusercontent.com/42258047/126596924-23e5500c-271d-4f1d-8787-ee9bee977f7f.png)
![image](https://user-images.githubusercontent.com/42258047/126596949-82c9b64f-c1f3-431c-81da-913f71260ee0.png)
![image](https://user-images.githubusercontent.com/42258047/126597185-a6ee47aa-5c94-434d-b5bb-2ba9dac2270f.png)
![image](https://user-images.githubusercontent.com/42258047/126597212-85051ba9-e0ef-493f-8598-31c3fad331a6.png)



### loss

| loss | loss_pose | loss_betas | loss_keypoints | loss_shape |
|:---:|:---:|:---:|:---:|:---:|
|<img src="https://user-images.githubusercontent.com/42258047/126597394-0d2d7ed0-1e7d-41e3-b93c-796fa94a14ac.png" width="250"> |<img src="https://user-images.githubusercontent.com/42258047/126597461-c723ed87-cd13-4389-b81d-457ff7afadff.png" width="250">| <img src="https://user-images.githubusercontent.com/42258047/126597542-6b9e5ef7-432b-4823-9a17-0dd8b4efc9df.png" width="250">  | <img src="https://user-images.githubusercontent.com/42258047/126597627-9704485c-04fa-4796-887c-c73c8454d42d.png" width="250"> |<img src="https://user-images.githubusercontent.com/42258047/126597496-2e424aed-5cd3-4d95-a4bb-dc4e09276826.png" width="250"> | 



### Evaluation Results

|  | 3dpw | mpi-inf-3dhp | h36m-p1 | h36m-p2 |
|:--:|:--:|:--:|:--:|:--:|
| MPJPE | 129.72 | 117.69 | 136.08 | 148.17 |
| Reconstruction Error | 70.66 | 78.10 | 77.73 | 77.57 | 


| | lsp | 
|:--:|:--:|
| Accuracy | 89.95 |
| F1 | 0.84 |
| Parts Accuracy | 87.29 |
| Parts F1 (BG) | 0.62 | 

#### Failure case
![image](https://user-images.githubusercontent.com/42258047/126597002-9c97e9ef-34b0-4154-b5cd-935963a96e9a.png)

![image](https://user-images.githubusercontent.com/42258047/126597014-7f0031cf-053f-4f5b-b049-8cc74b7ae061.png)

![image](https://user-images.githubusercontent.com/42258047/126597041-83ddf704-a6d6-4571-a51c-3b7dace803ea.png)

![image](https://user-images.githubusercontent.com/42258047/126597058-40a417cf-764b-4144-aeba-fc78ae1a334c.png)

![image](https://user-images.githubusercontent.com/42258047/126597141-04788676-f0f3-4429-a4ca-8f4b2649e400.png)






### Question 

 아래 train options에서도 알 수 있지만, shape_loss weight가 0으로 되어있어서 loss에서 shapeloss에는 0이 곱해지는데
  shapeloss는 어케 계속 optimize되는건가..?


### train options

train_add_smple_loss4 


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

### train time 

training 시작시간이 20210720 23:20 즈음임. 
끝난게 얼추 21일 23시 50분 이니, 24시간 정도 걸린 것 같다. 


### train parameter

![image](https://user-images.githubusercontent.com/42258047/126589259-f621b89b-943f-434e-ab1d-6833e3c581e7.png)

위에 사진은 왜 저렇고,, 밑에는 따로 count하는 함수를 만들어서 샌건데..
왜 둘이 다른지 잘 모르겠다. 

총 26,977,501

