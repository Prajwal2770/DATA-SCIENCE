import numpy as np
    
matrix=np.array([[100,200,300],[400,500,600]]) # 2x3 matrix
vector=np.array([10,20])
arr_1=vector.reshape(2,1)
res=matrix+arr_1
print(res)
