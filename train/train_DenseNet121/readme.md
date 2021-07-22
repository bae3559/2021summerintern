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



