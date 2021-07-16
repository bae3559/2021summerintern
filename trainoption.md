## List of Train Options

### Required!!!!!!!!
--name 'Name of the experiment'

### General
--time_to_run 'Total time to run in seconds. Used for training in environments with timing constraints'
--resume 'Resume fromm checkpoint (Use latest checkpoint by defuault)'
--num_workers 'Number of processes used for data loading'
--pin_memory ???
--no_pin_memory ???

### io 
--log_dir 'Directory to store logs' default = logs
--checkpoint 'Path to checkpoint' default = None
--from_json 'Load options from json file instead of the command line' default = None
--pretrained_checkpoint 'Load a pretrained checkpoint at the beginning training'

### Training Options
--num_epochs 'Total number of training epochs' default = 50
--lr 'Learning rate' default = 5e-5
--batch_size default = 64
--summary_steps 'Summary saving frequency' default = 100
--test_steps 'Testing frequency during training' default = 1000
--checkpoint_steps 'Check point saving frequency' default = 10000
--img_res 'Rescale bounding boxes to size [img_res, img_res] before feeding them in the network' default = 224 (resnet is constructed with input size 3x224x224)

--rot_factor 'Random rotation in the range [-rot_factor, rot_factor] default = 30

### 어디서 쓰이는지 확인해보기 
--noise_factor 'Randomly multiply pixel values with factor in the range [1-noise_factor, 1+noise_factor]'  default = 0.4 ???????????? 

--scale_facgtor 'Rescale multiply pixel values with factor in the range [1-scale_factor, 1+scale_factor]'
--ignore_3d 'Ignore GT 3D data for unpaired experiments' defualt = False
--shape_loss_weight 'weight of per-vertex loss' default = 0
--keypoint_loss_weight 'weight of 2D and 3D keypoint loss' default = 5
--pose_loss_weight 'weight of SMPL pose loss' default = 1
--beta_loss_weight 'weight of SMPL beta loss' default = 0.001
--openpose_train_weight 'Weight for OpenPose keypoints during training' default = 0
--gt_train_weight 'Weight for GT keypoints during training' default = 1
--run_smplify 'Run SMPLify during training' default = False
--smplify_threshold 'Threshold for ignoring SMPLify fits during training' default = 100
--num_smplify_iters 'Number of SMPLify iteration' default = 100

### Data set Shuffle 여부

--shuffle_train 
--no_shuffle_train
