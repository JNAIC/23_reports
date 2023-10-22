import numpy as np
"""numpy用来处理数组，数组对象称为ndarray"""

#使用array()函数可以创建ndarray对象
arr=np.array([1,2,3,4,5])
print(arr)
print(type(arr))

#0-D数组
arr=np.array(13)
print(arr)

#1-D数组
arr=np.array([1,3,5,7,9])
print(arr)

#2-D数组,包含两个数组
arr=np.array([[1,2,3],[4,5,6]])
print(arr)

#3-D数组，元素为2—D
arr=np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr)

"""检查维数，使用ndim()"""
a=np.array([1,3,4])
print(a.ndim)

