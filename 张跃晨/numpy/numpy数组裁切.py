import numpy as np
"""与列表的切片方式类似,[start:end:step]"""
arr=np.array([1,2,3,4,5,6,7])
print(arr[1:5])
print(arr[1:6:2])

"""裁切二维数列,注意使用逗号隔开"""
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[1,1:3])

