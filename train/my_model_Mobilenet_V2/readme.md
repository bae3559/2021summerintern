# Actual Mobilenetv2


### Evaluation Results

|  | 3dpw | mpi-inf-3dhp | h36m-p1 | h36m-p2 |
|:--:|:--:|:--:|:--:|:--:|
| MPJPE | 138.997 | 129.7836 | 146.32 | 150.74 |
| Reconstruction Error | 79.743 | 89.40 | 86.12 | 86.73 | 


| | lsp | 
|:--:|:--:|
| Accuracy | 87.93 |
| F1 | 0.7999 |
| Parts Accuracy | 85.04 |
| Parts F1 (BG) | 0.5326 | 

# My Mobilenetv2

# Parameters 3131853

### Evaluation Results

|  | 3dpw | mpi-inf-3dhp | h36m-p1 | h36m-p2 |
|:--:|:--:|:--:|:--:|:--:|
| MPJPE | 140.70690 | 129.98987 | 151.055673 | 159.322326 |
| Reconstruction Error | 78.99198 | 87.5197 | 87.028878 | 87.49994 | 


| | lsp | 
|:--:|:--:|
| Accuracy | 0.88648088211 |
| F1 |  0.81372374893 |
| Parts Accuracy |  0.85822870 |
| Parts F1 (BG) | 0.561458081 |

# After pruning1 & finetuning 
pruning ( 20% )
## finetuning 20 epochs

inference time :  0.0005920188426624291 s

mpi inf 기준으로 time.time썼을 때 1.1ms, cuda.event & torch.cuda.synchronize() 사용 했을 때 945ms ?
h36m-p1 time.time 썼을 때 0.592 ms, cuda.event & torch.cuda.synchronize() 1s

mpi-inf-3dhp torch.cuda.synchronize() + time.time() 쓰면, 0.0007758 s = 0.7ms
뭔가 inference time이 제각각이고 그때그때 달라서 비교하기가 애매하다..

### Evaluation Results

|  | 3dpw | mpi-inf-3dhp | h36m-p1 | h36m-p2 |
|:--:|:--:|:--:|:--:|:--:|
| inference time |  | 1.1 ms | 0.592 ms | 1.048 ms |
| MPJPE | 144.45 | 128.3293 | 147.6520 | 160.9229 |
| Reconstruction Error | 81.2267 | 85.376 | 84.73537 | 86.4256 | 

lsp inference time 1.256s 
| | lsp | 
|:--:|:--:|
| Accuracy | 0.889767 |
| F1 | 0.82004 |
| Parts Accuracy | 0.86139 |
| Parts F1 (BG) | 0.569655 |

# After pruning2 & finetuning 
+ pruning 20%
# fintuning 10epoch
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

# fintuning 20epoch
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
