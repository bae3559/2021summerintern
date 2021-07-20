처음부터 바로 spin 코드 전체를 training 시키면 이해하는데 어려움이 있을 것 같아서, 
하나씩 추가해보면서 해보기로 했다. 

#### 1. joint가 제대로 가는지 정도를 보려고 일부러 keypoint_loss, keypoint_3d_loss 만 사용해보았다.

결과가 굉장히 기괴하다...전체적인 모양 자체는 비슷하지만, 팔이 여러번 꼬여있거나 한 형태로
beta와 theta가 이상한 값이라는 것을 알 수 있다.

#### 2. 그리고 n_iter 부분 즉 regression 부분이 어떤 영향을 미치는지 알고 싶어서 n_iter을 첨에 1로 놓고 해봤다..

근데 딱히 지금 생각해보니 이후에 여러가지 문제를 해결했는데 그 때문에 다시 해봐야 알 수 있을 것 같다.

#### 3. shape과 pose를 update해주기위해 loss들을 각각 추가해줬는데, has_smpl에서 문제가 생겼다.

이는 mixed_dataset에서 indexing issue가 있었던 것이다...

0720날짜로 학습 중 이다. 결과는 내일 업로드 할 것.


-----------------------------------------------------------------------------------------------------------

| name | options | results |
|:---|---:|:---:|
| train_test | my_model()에서 n_iter을 없앤 것 | |
| train_add_regression | my_model()에서 for (n_iter=3)문을 추가한 것. (regression부분) | 딱히 학습이 잘 안됨 |
train_add_regression2 | 위와 동일 , batch_size = 100으로 수정 | 모양은 어느정도 맞지만, 기괴한 모양... beta랑 pose를 학습 안 시켰으니까 당연한 결과
train_add_smpl_loss | 이번에는 smpl loss 들을 추가함. | 근데 이상하게 중간에 22epoch중에 에러가 뜸. 
train_add_smpl_loss2 | 위와 동일하게 2트 | 하지만 마찬가지로 loss가 너무 큼. 그리고 pose, beta가 전혀 업데이트가 안되는 것 같음.
train_add_smpl_loss3 | 이것 저것 문제점을 고침. has_smpl이라는 값이 이상하게 다 0이었는데 이는 mixed dataset에서 indexing을 0부터 시작하도록 고쳐줌. 그리고 tqdm 부분을 조금 고쳐서 각 loss들이 같이 progress bar에 나타나게 수정함. | 중간에 결과를 확인했는데 일단 keypoint loss랑 loss 자체가 너무 너무 커서 ... 뭔가 ..이상함..  이유 중 하나로 생각 되는 것은 내가 pretrained resnet을 안쓰고 쌩으로 다 하려해서..그랬던 것으로 알게 되어 4는 pretrained 부분을 Trure로 다시 고쳐서 시도 함. 
train_add_smpl_loss4 | mymodel() 부분에서 pretrained=True로 다시 고쳤다. | 현제 0720날짜로 11시쯤 시작함. loss값은 약 14-20 사이로 정상적인 것 같음.. 위에서는 e7까지 같던 것을 생각함ㄴ 매우 정상적. 
