DenseNet169 를 Encoder로 사용하면서 regression 부분을 바꾸어보았다.

원래 한 번 iteration 돌 때, FC layer을 두 번 거치는데 

이번에 fc2를없애고 진행해 보았다. 

loss

![image](https://user-images.githubusercontent.com/42258047/127769840-d5f95f8f-8f34-44d5-8baa-7deabe4c48d3.png)

keypoint loss

![image](https://user-images.githubusercontent.com/42258047/127769852-24a51843-7a6f-4a8c-ba93-75c58105616f.png)

beta loss

![image](https://user-images.githubusercontent.com/42258047/127770024-a1a54b52-8f79-4d09-8ba7-5480fed0f91d.png)

pose loss

![image](https://user-images.githubusercontent.com/42258047/127770062-933f02b5-046f-46fd-a103-13e1ad35e872.png)

shape loss

![image](https://user-images.githubusercontent.com/42258047/127770075-b56fb0d5-38f6-4fec-b72f-2e73e78b5696.png)


### Evaluation Results

|  | 3dpw | mpi-inf-3dhp | h36m-p1 | h36m-p2 |
|:--:|:--:|:--:|:--:|:--:|
| MPJPE | 125.9358 | 118.0348 | 130.0594 | 141.0075 |
| Reconstruction Error | 76.1138 | 78.8814 | 76.6511 | 76.2778 | 


| | lsp | 
|:--:|:--:|
| Accuracy | 89.7898 |
| F1 | 0.8347 |
| Parts Accuracy | 87.0775 |
| Parts F1 (BG) | 0.6056 | 



### final results

![image](https://user-images.githubusercontent.com/42258047/127769800-d7267a34-5170-496f-9e5a-e6745d058bba.png)
![image](https://user-images.githubusercontent.com/42258047/127769812-9091de0a-8a56-404f-b622-1264c1ed9e60.png)
![image](https://user-images.githubusercontent.com/42258047/127769817-3cc495be-691b-4756-8624-dd4b10e052f8.png)
![image](https://user-images.githubusercontent.com/42258047/127769829-66172549-ebc6-4039-8bd9-6b06abc83bbb.png)
