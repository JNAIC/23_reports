import numpy as np
"""使用concatenate()函数连接数组"""
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr=np.concatenate((arr1,arr2))
print(arr)
print("\n")

"""利用axis=1连接二维数组"""
arr3 = np.array([[1, 2], [3, 4]])
arr4 = np.array([[5, 6], [7, 8]])
arr_2=np.concatenate((arr3,arr4),axis=1)
print(arr_2)
print("\n")

"""使用stack()函数按照新轴连接数组"""
a = np.array([[1,2,3,4,5],[3,4,5,6,7]])
b = np.array([[5,6,7,8,9],[7,8,9,10,11]])
print(np.stack((a,b),axis=0))
print("\n")
print(np.stack((a,b),axis=1))
print("\n")

"""使用hstack()按照行堆叠数组"""
a = np.array([[1,2,3,4,5],[3,4,5,6,7]])
b = np.array([[5,6,7,8,9],[7,8,9,10,11]])
print(np.hstack((a,b)))
print("\n")

"""使用vstack()按照列堆叠数组"""
a = np.array([[1,2,3,4,5],[3,4,5,6,7]])
b = np.array([[5,6,7,8,9],[7,8,9,10,11]])
print(np.vstack((a,b)))
print("\n")

"""使用dstack()按照高度堆叠数组"""
a = np.array([[1,2,3,4,5],[3,4,5,6,7]])
b = np.array([[5,6,7,8,9],[7,8,9,10,11]])
print(np.dstack((a,b)))