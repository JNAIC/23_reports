import numpy as np

"""使用dtype返回数组的数据类型"""
arr = np.array([1, 2, 3, 4])
print(arr.dtype)

"""用已经创建的数据类型定义数组"""
arr=np.array([1,3,5,7,9],dtype="S")
print(arr)
print(arr.dtype)