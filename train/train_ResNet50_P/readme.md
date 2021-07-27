각 layer의 conv 마다 prunning을 해주었다. 

전체 20% 에 prunning을 했다. 

우선 현지 오후 5시 기준으로 학습을 시작했다. 

지난번 24시간이 걸린것과 얼마나 차이가 날지는 해봐야 알 수 있을 듯 하다. 

실제로 prunning을 덧붙인 것 만으로 학습시간에 차이가 있는지는 궁금하긴하다. 

성능에도 차이가 있는지는 결과를 봐야 알 수 있을 것 같다. 

prunning을 하는 코드는 [예제 사이트](https://github.com/Huffon/nlp-various-tutorials/blob/master/pruning-bert.ipynb)를 참고 하였다.

이외의 다른 train option들은 이전 [train_smpl_lossr4](https://github.com/bae3559/2021summerintern/tree/main/train/train_add_smpl_loss4) 와 동일하다. 


### Results

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
