확실히 mobilenetv3_large가 오히려 mobilenetv2보다 잘 안나와서 이상하다 생ㄱ가했는데 오히려 pruning 이후에 성능이 증가하는걸 볼 수 있었다. 

한 번 더 pruning 해봐도 괜찮을 듯 하다. 

그리고 그림들을 봤을 때 느낌은 3d보다는 확실ㅇ히 2d를 잘 맞추는 느낌이었다. 


# Before pruning

### Evaluation Results

|  | 3dpw | mpi-inf-3dhp | h36m-p1 | h36m-p2 |
|:--:|:--:|:--:|:--:|:--:|
| MPJPE | 153.30209 | 133.4778 | 155.3194 | 170.3679 |
| Reconstruction Error | 85.9931 | 89.63268 | 90.3116 | 91.5088 | 


| | lsp | 
|:--:|:--:|
| Accuracy |  |
| F1 |  |
| Parts Accuracy |  |
| Parts F1 (BG) |  |



# pruning Results


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


# After fine-tuning 


### Evaluation Results

|  | 3dpw | mpi-inf-3dhp | h36m-p1 | h36m-p2 |
|:--:|:--:|:--:|:--:|:--:|
| MPJPE | 149.4617 | 128.1594 | 153.27958 | 170.12446 |
| Reconstruction Error | 84.31569 | 84.86604 | 87.49703 | 88.0245 | 



| | lsp | 
|:--:|:--:|
| Accuracy | 0.89675597 |
| F1 | 0.83494619 |
| Parts Accuracy | 0.8663722 |
| Parts F1 (BG) | 0.593974122 |

