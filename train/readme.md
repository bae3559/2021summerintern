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


#### 이후 encoder 부분의 resnset50을 다양하게 바꿔가면서 test해보고 있다. 


#### Parameter 

| method | resnet50 | densenet121 | densenet169 | densenet201 | MobileNetV2 | MobileNetV3 | ShuffleNetV2_X1.0 |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
|Parameter | 26,977,501 | 3,494,447 | 16,545,797 | 22,410,245 | 5,901,189 |  | 4,674,921 |

#### mpi-inf-3dhp

| method | resnet50 | densenet121 | densenet169 | densenet201 | MobileNetV2 | MobileNetV3 | ShuffleNetV2_X1.0 |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| MPJPE | 117.69 | 287.97 | 112.89 | 115.5370 | 129.7836 |  |  |
| Reconstruction Error | 78.10 | 142.93 | 76.54 | 76.7496 | 89.40 |  |  |

#### 3dpw

| method | resnet50 | densenet121 | densenet169 | densenet201 | MobileNetV2 | MobileNetV3 |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| MPJPE | 129.72 | 273.95 | 121.13 | 133.7542 | 138.997 |  |
| Reconstruction Error | 70.66 | 127.44 | 71.37 | 74.77 | 79.743 |  |



#### prunning results

| method | resnet50 | pruning resnet50 |
|:--:|:--:|:--:|
|  |  |  |




#### lsp 



-----------------------------------------------------------------------------------------------------------

| name | options | results |
|:---:|:---:|:---:|
| train_test | my_model()에서 n_iter을 없앤 것 | |
| train_add_regression | my_model()에서 for (n_iter=3)문을 추가한 것. (regression부분) | 딱히 학습이 잘 안됨 |
| train_add_regression2 | 위와 동일 , batch_size = 100으로 수정 | 모양은 어느정도 맞지만, 기괴한 모양... beta랑 pose를 학습 안 시켰으니까 당연한 결과
| train_add_smpl_loss | 이번에는 smpl loss 들을 추가함. | 근데 이상하게 중간에 22epoch중에 에러가 뜸. 
| train_add_smpl_loss2 | 위와 동일하게 2트 | 하지만 마찬가지로 loss가 너무 큼. 그리고 pose, beta가 전혀 업데이트가 안되는 것 같음.
| train_add_smpl_loss3 | 이것 저것 문제점을 고침. has_smpl이라는 값이 이상하게 다 0이었는데 이는 mixed dataset에서 indexing을 0부터 시작하도록 고쳐줌. 그리고 tqdm 부분을 조금 고쳐서 각 loss들이 같이 progress bar에 나타나게 수정함. | 중간에 결과를 확인했는데 일단 keypoint loss랑 loss 자체가 너무 너무 커서 ... 뭔가 ..이상함..  이유 중 하나로 생각 되는 것은 내가 pretrained resnet을 안쓰고 쌩으로 다 하려해서..그랬던 것으로 알게 되어 4는 pretrained 부분을 Trure로 다시 고쳐서 시도 함. 
|train_add_smpl_loss4 | mymodel() 부분에서 pretrained=True로 다시 고쳤다. | 현제 0720날짜로 11시쯤 시작함. loss값은 약 14-20 사이로 정상적인 것 같음.. 위에서는 e7까지 같던 것을 생각함ㄴ 매우 정상적. |
| train_DenseNet121 | resnet 을 backbone 으로 한 위 학습들이랑 다르게 이번에는 Densenet 121을 백본으로 한 학습을 진행해보았다. 확실히 parameter 수가 엄청나게 차이난다. | 지금은 1epoch 돌고 있는데 위와 마찬가지로 loss 가 14-25 사이인거 같고 학습이 잘 될지는 해봐야 알 수 있을 듯 하다. | 
| train_DenseNet169 | DenseNet169는 딱히 성능이 나오진 않았다. 실제로 loss도 그리 많이 낮아지지 않았고, 그래서 이번에는 DenseNet 169로 진행해보고자 한다. 파라미터 수 거의 1/2 넘게 작음! | resnet50 보다 성능도 좋다!  |
| train_DenseNet201 | parameter 수 22410245 | |
| train_ResNet50_P |  resnet 50에 전체 sparsity 20%로 prunning을 적용시켰는데, 성능이 좋지 않았다....| |
| train_MobileNetV2 | 그래서 다른 네트워크에 prunning을 적용시켜보는 것 보다 더 parameter가 작은 network를 실행시켜보려한다. 개수는 DenseNet121보다는 작지만 지금까지 Parameter에 비해 매우 작은 편이라 성능만 잘 나와준다면 좋겠다.  |  |



근데 무슨 이유인진 몰라도 169 부터는 계속 CUDA out of memory로 인해서 ,, batchsize를 줄이고 잇따. 

----------------------------------------------------------------------------------------------------

## DenseNet
Densenet 121을 backbone으로 해서 학습을 진행해보고자 한다. 

실제로 parameter 수는 resnet보다 줄이면서 성능은 높거나 그 비슷하게 나왔던 이전 논문들의 결과를 보면서 

resnet 부분을 한 번 바꿔보는 시도도 재밌을 것 같다고 생각해서 직접 해보고 있다.

문제는 지금 일단 학습 시키는데 너무 오랜 시간이 걸리다 보니 급하게 densenet을 끼워 넣어서 학습을 돌리고 있는데, 

densent을 정확하게 이해하고 코딩을 한 것이 아니라서 어떤 오류를 범했을지는 나도 잘 모르겠다. 

![image](https://user-images.githubusercontent.com/42258047/126596370-1bb03657-8809-4f86-991b-ff74fc859a71.png)

위 사진을 기반으로 하여 우선 densent 121을 돌려보았고, 

잘 되면 densenet 169 를 시도해볼 계획이다. 

이후 어느정도 accuracy가 보장된다면, 

여기에서 prunning을 더 해보는 시도도 해보려한다. 

사실 Densenet이 cvpr 2017 bestpaper이고, hmr이 cvpr2018 이었던 걸 생각해보면

densenet이 아니라 resnet을 쓴 이유가 있을 것 같기도하다. 

하지만 직접 실험해보고 결과를 보고 싶어서 해보는 것이니, 큰 기대는 말자. 


## Prunning

위에서 지금까지 시도해본 여러 Encoder에 이제 prunning을 적용시켜보려한다.

여기서부터 할 수 있는게 너무 여러가지 인 것 같아서 고민을 조금 많이 했다. 

왜냐하면, 이제 discriminator 을 더 붙여볼 것 인지, encoder을 최대한 더 가볍게 만든 다음에 discriminator을 붙일 건지! 를 고민을 하다가, 

우선 encoder을 더 가볍게 만들어보고자 한다. 

그래서 성능이 떨어지는 한이 있더라도 일단 더 가볍게 ? 만들어보는 것과, prunning을 한번 구현해보는 시간을 가지고자 한다. 

DensNet201에는 적용시켜봐도 괜찮을 것 같다. 

## MobileNet

![image](https://user-images.githubusercontent.com/42258047/127288334-73c2b193-e0fa-4b20-98be-a13b8f88eec0.png)



Prunning이 딱히 성능 향상에는 효과가 없었다. 

경량화를 하는데에는 충분한 효과가 있었으며, 그렇다고 성능을 떨어뜨리는 정도도 아니었으니 후에 모델을 만든 후 
경량화를 하는 방법으로 사용하는 것으로 좋을 것 같다고 생각한다. 

이후 새로운 실험을 위해 MobileNetV2를 이용해서 training을 시키고 있다. 
이 Network 또한 매우 가벼운편이며 파라미터 수와 memory모두 적게 사용하는 것을 알 수 있다. 

따라서 성능을 확인해보고 DenseNet169보다 좋은지 비교해보고자 한다. 

성능이 DenseNet169 만큼 나오지는 않았다. 하지만 MobileNetV2보다 MobileNetV3가 훨씬 성능이 좋았던 만큼 MobileNetV3 - large로 테스트해보려한다. 

---------------------------------------------------------------------------------------------------

## ISSUE

__1. GPU 0번에 계속 조금씩 allocate 됨__

<img src="https://user-images.githubusercontent.com/42258047/126368627-bedc572e-c344-444f-8399-0a4653659db3.png" width="400">

위 사진을 통해 알 수 있듯이 현재, 나는 2번 GPU를 쓰도록, 다른 사람은 7번을 쓰도록 코드를 작성하고 
코드를 실행 시켰는데 항상 0번에 10MiB 정도는 allocate 되는 것 같은 issue가 있다. 

__2. GPU-Util이 계속 0으로 돌아감__

아마 tensorboard에 업로드 하는 과정 및 dataloading 과정에서 CPU를 사용하는 것 같다. 그런데 그게 생각보다 오래 걸린다. 

5epoch을 도는 동안 3시간이 걸렸음. 

이 속도면 50epoch이면 30시간이 걸린다는... 
이전 ( train_add_smpl_loss4 이전 ) 까지는 한 10시간 정도 걸린 것을 생각하면,, 그 동안 정말 제대로 학습이 안되고 있었기 때문이거나
현재 gpu를 제대로 활용하지 못하고 있어서 연산이 느린 것 같다. 
