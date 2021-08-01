** 버전상의 문제로 MobileNetV3는 pretrained된 모델을 사용하지 않았다. **

scratch로 처음부터 학습시켰다. 

loss

![image](https://user-images.githubusercontent.com/42258047/127738197-b1281e10-d210-4717-b6b3-bf35989d9690.png)

keypoint loss 

![image](https://user-images.githubusercontent.com/42258047/127738208-d3a58d5b-dbf1-4ae0-b948-d3c7f64a1231.png)

regr betas loss

![image](https://user-images.githubusercontent.com/42258047/127738219-676c46e1-fbbf-40cb-afb6-73fdf1e5edd1.png)

regr poss loss

![image](https://user-images.githubusercontent.com/42258047/127738234-1e52847e-d87f-4f6b-9be1-9c3438c3e9f0.png)

regr shape loss 

![image](https://user-images.githubusercontent.com/42258047/127738245-76ef18ba-2d8a-4cc4-9169-7017299ca032.png)




### Evaluation Results

|  | 3dpw | mpi-inf-3dhp | h36m-p1 | h36m-p2 |
|:--:|:--:|:--:|:--:|:--:|
| MPJPE |  |  |  |  |
| Reconstruction Error |  |  |  |  | 


| | lsp | 
|:--:|:--:|
| Accuracy |  |
| F1 |  |
| Parts Accuracy |  |
| Parts F1 (BG) |  | 

### Final Results

![image](https://user-images.githubusercontent.com/42258047/127738165-f83ba9fc-2eae-46fc-921e-dc2e5b912b88.png)
![image](https://user-images.githubusercontent.com/42258047/127738175-c601021c-b005-404b-bf4a-1bd55c784d61.png)
![image](https://user-images.githubusercontent.com/42258047/127738183-ed9fe609-5f93-4b83-aa27-30b9158a30a9.png)
![image](https://user-images.githubusercontent.com/42258047/127738185-c8536ebc-d720-4fc1-a775-bdd5888cb8aa.png)
![image](https://user-images.githubusercontent.com/42258047/127738192-b1982b4e-6660-41b2-827b-b47e49fb55c0.png)
