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

### Final Results

![image](https://user-images.githubusercontent.com/42258047/127287245-6ac25844-b629-454d-9ae6-c2aca20473ba.png)
![image](https://user-images.githubusercontent.com/42258047/127287012-aecc1922-ef91-49a2-b32e-a5ca1197256e.png)
![image](https://user-images.githubusercontent.com/42258047/127287083-c98c8c27-df8b-4969-8266-772918aaf357.png)
![image](https://user-images.githubusercontent.com/42258047/127287146-45cded92-0733-4e3e-a715-c0a0fc1d151f.png)

### Failure case

![image](https://user-images.githubusercontent.com/42258047/127287193-853f2a8f-08d2-478c-9a8e-c9adcfb67101.png)
![image](https://user-images.githubusercontent.com/42258047/127287320-328e4139-530c-492e-ac5c-a647ee46164b.png)


