# np.nan_to_num(array,nan=value) default=0
import numpy as np

arr=np.array([1,2,np.nan,4,np.nan,6])
print(arr)
print(np.isnan(arr))
cle_arr=np.nan_to_num(arr) # if not passed default =0
print(cle_arr)

cl_arr=np.nan_to_num(arr,nan=5)
print(cl_arr)
