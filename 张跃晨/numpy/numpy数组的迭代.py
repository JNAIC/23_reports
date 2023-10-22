import numpy as np
#迭代意味着遍历

"""使用for遍历，像pyhton一样"""
#一维
arr = np.array([1, 2, 3])
for x in arr:
    print(x)
#二维
arr2= np.array([[1, 2, 3], [4, 5, 6]])
for x2 in arr2:
  print(x2)

for x2 in arr2:
   for y in x2:
       print(y)

"""使用nditer直接迭代高维数组"""
arr3= np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in np.nditer(arr3):
    print(x)

"""迭代时更改数据类型，使用op_dtypes传递期望的数据类型，同时需要额外空间buffer"""
arr4= np.array([1, 2, 3])
for i in np.nditer(arr,flags=["buffered"],op_dtypes=["S"]):
   print(i)

"""以不同步长迭代"""
arr5= np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for i2 in np.nditer(arr5[:,::2]):
   print(i2)

"""枚举迭代，可以带出来索引，使用ndenumerate()"""
arr6= np.array([1, 2, 3])
for idx,x0 in np.ndenumerate(arr6):
   print(idx,x0)