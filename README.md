# 2021summerintern

# 20210705_mon

1. seminar 
1) cross modal representation learning 

  두가지 이상의 데이터가 주어졌을 때, 한 가지를 기반으로 나머지 한가지 정보를 배우는 등의 방식. 
  쉽게 예로 vision(시각)과 audio(청각)의 데이터 두 가지를 주었을 때 오디오를 듣고 오디오에 해당하는 이미지 찾기(cross modal retriever) 과 같이 비슷하다 생각하면 된다. 
  
  본 논문에서는 modality independent 한 encoder 을 사용하였다. 이건 결국 각각 vision과 auidio 각각의 두 가지 데이터를 각각 다른 encoder를 통과시켰다고 생각하면 된다. 
  이후 joint embedding space에서 만나 positive pair끼리 같아지게, negative pair끼리 같아지게 MMS Loss를 적용하였다. 
  추가적으로 만든 embedding space에서 VQ block을 통과시킨다. 이 때, code book을 사용하였고 code book의 initialization 은 가우시안을 하였다.
  
2) Neural Design Network : Graphic Layout Generation with constraints 

  component와 layout을 이용해 괜찮은 graphic constraints을 뽑아내는 연구이다.
  
  related works에는 Natural scen layout generation, graphic design layout generation 등이 있다. 
  
2. HMR demo

HMR demo를 ubuntu에서 실행해보려 하였으나, tf2로 하면 뭐가 안돼고, tf1으로 하면 뭐가 에러가 나고 해서
일단은 내일 윈도우에서 해보고 또 안되면 colab으로 해볼 계획이다.


# 20210706_(tue)

1. 
2. 
