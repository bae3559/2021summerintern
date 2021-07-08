# 2021summerintern

### 20210705_mon

__1. seminar__
1 ) cross modal representation learning 

  두가지 이상의 데이터가 주어졌을 때, 한 가지를 기반으로 나머지 한가지 정보를 배우는 등의 방식. 
  쉽게 예로 vision(시각)과 audio(청각)의 데이터 두 가지를 주었을 때 오디오를 듣고 오디오에 해당하는 이미지 찾기(cross modal retriever) 과 같이 비슷하다 생각하면 된다. 
  
  본 논문에서는 modality independent 한 encoder 을 사용하였다. 이건 결국 각각 vision과 auidio 각각의 두 가지 데이터를 각각 다른 encoder를 통과시켰다고 생각하면 된다. 
  이후 joint embedding space에서 만나 positive pair끼리 같아지게, negative pair끼리 같아지게 MMS Loss를 적용하였다. 
  추가적으로 만든 embedding space에서 VQ block을 통과시킨다. 이 때, code book을 사용하였고 code book의 initialization 은 가우시안을 하였다.
  
2 ) Neural Design Network : Graphic Layout Generation with constraints 

  component와 layout을 이용해 괜찮은 graphic constraints을 뽑아내는 연구이다.
  
  related works에는 Natural scen layout generation, graphic design layout generation 등이 있다. 
  
__2. HMR demo

HMR demo를 ubuntu에서 실행해보려 하였으나, tf2로 하면 뭐가 안돼고, tf1으로 하면 뭐가 에러가 나고 해서
일단은 내일 윈도우에서 해보고 또 안되면 colab으로 해볼 계획이다.


### 20210706_(tue)

__1. colab에서 HMR demo 실행


1 ) HMR file download ( hmr-master.zip )
2 ) colab 켜서 파일 업로드 이후 
``` 
 !unzip --q /content/hmr-master.zip 
```
3 ) tensorflow 1.3.0  깔기

( 이미 2가 설치 되어있다면 unninstall 이후 1.3.0으로 재 설치)

단 opendr 0.77 먼저 받을 것 - 아니면 tensorflow=1.3.0을 깔 수 없음 , hmr github issue에 나와있는 설명

4 ) 이후 requirements.txt 에 있는 애들 다운로드 후 데모 실행해보기 
```
!pip2 install -r requirements.txt'
!python2 demo --img_path data/coco1.png
```

에러는 안 나지만, <Figure size 640x480 with 6 Axes>만 나오고 그림이 안보임. 

__2. 수요일 세미나 때 발표하는 논문들 미리 한 번 더 훑어 보기!

### 20210707_(wed)

__1. 연참생들 세미나
1) Keep it SMPL : Automatic Estimation of 3D human pose and Shape from a single Image
2) End to end Recovery of Human Shape and Pose
3) Generative Adversarial Networks

__2. 오늘도 다시 데모를 실행해보려했으나 실패. 오늘은 docker를 설치해보았다. 
docker를 어떻게 쓰는지 정확하겐 모르겠어서 그런지 실패! ㅜ 
 
tensorflow1을 쓰는건 너무 오래 전 것이라, 선배한테 환경 설정을 어케 했냐고 물어본 결과, 
SPIN github를 들어가서 살펴보라고 하셨다! 
SPIN 은 pytorch, python3 로 되어있기 때문에 이후에 코딩할 때도 편할 것이라고...

### 20210708_(thu)

__1. HMR 논문 다시 읽기 

HMR을 몇 번 읽었더니 이제 조금 알 것 같은데 몇 개 질문이 생겼다. 

q1. Figure2에는 camera 관련 파라미터로 T가 있는데, 실제로 본문에 설명에서는 s, R, t로 하나씩 설명이 되어있다. T=t인건가?

q2. 본문 중 'The 3D key points used for reprojection error, X(theta, beta) R^(3xp) , are obtained by linear regression from the final mesh vertices. 
여기서 P가 갑자기 어디서 나온 값인지 잘 모르겠다. P? joint 개수 인걸까? X()는 3차원 joints들이 아닌가?

__2. pyrender 예제 공부
SPIN이랑 HMR 코드를 조금씩 살펴보다가, pyrender와 pytorch를 이해해야 코드를 보기 편할 것 같다고 생각했다. 
pyrender를 실행시키는 환경은 그리 문제가 되지는 않았다. colab에서 실행시켜보았고, 
https://pyrender.readthedocs.io/en/latest/examples/quickstart.html 을 참고하여 여러 가지 rendering을 해보았다. 
 
잊지 말고 런타임 유형 GPU로 바꾸기~ 

```
import os
os.environ["PYOPENGL_PLATFORM"] = "egl" #opengl seems to only work with TPU
!PYOPENGL_PLATFORM=egl python -c "from OpenGL import EGL"
print(os.environ['PYOPENGL_PLATFORM']) 
```
그리고 이거 설치랑, 
requirements 설치할 때, pyglet==1.4.0b1로 바꿔서 하기!

*근데 문제는 pyrender.Viewer()이 안되는데 왜,,안되는지 모르겠다.


