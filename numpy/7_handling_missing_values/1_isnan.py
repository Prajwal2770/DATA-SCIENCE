import numpy as np

arr=np.array([1,2,np.nan,4,np.nan,6])
print(arr)
print(np.isnan(arr))


# we cant compare it directly
# print(np.nan==np.nan) 