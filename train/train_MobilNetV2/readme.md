### Parameters 

5,901,189


7월 27일 오후 3시 30분 경 학습을 시작했고, GPU memory를 약 4517MiB 정도 사용하는 것으로 보아 가벼운 model임을 알 수 있다.
오후 4시 30분 완료 근데 왤케 오래 걸린거지? 


### Loss
| loss | loss_pose | loss_betas | loss_keypoints | loss_shape |
|:---:|:---:|:---:|:---:|:---:|
|<img src="https://user-images.githubusercontent.com/42258047/127283226-5dbc29d5-a653-48a9-b7e2-7754e01fb7e8.png" width="300"> | <img src="https://user-images.githubusercontent.com/42258047/127283601-ddbe2ed4-3b91-43da-b037-ca575fc37bd6.png" width="300"> | <img src="https://user-images.githubusercontent.com/42258047/127283377-a60250c5-1537-429e-89b1-615bd43b3a25.png" width="300"> | <img src="https://user-images.githubusercontent.com/42258047/127283289-149da840-f47e-4492-8c41-e9fce5eedf11.png" width="300"> | <img src="https://user-images.githubusercontent.com/42258047/127283526-e9abbc62-f7c6-4b20-a121-b42da54424a2.png" width="300">| 


### Evaluation Results

|  | 3dpw | mpi-inf-3dhp | h36m-p1 | h36m-p2 |
|:--:|:--:|:--:|:--:|:--:|
| MPJPE | 138.997 | 129.7836 |  |  |
| Reconstruction Error | 79.743 | 89.40 |  |  | 


| | lsp | 
|:--:|:--:|
| Accuracy | 87.93 |
| F1 | 0.7999 |
| Parts Accuracy | 85.04 |
| Parts F1 (BG) | 0.5326 | 
