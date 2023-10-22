import numpy as np
"""使用where()方法搜索数组中的值，并返回索引"""
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x=np.where(arr==4)
print(x)
print("\n")
#查找值为偶数的索引
arr2 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y=np.where(arr2%2==0)
print(y)

"""使用searchsorted()选择一个合适的位置插入元素并返回索引"""
arr2 = np.array([6, 7, 8, 9])
x=np.searchsorted(arr2,7)
print(x)
print("\n")
#从右向左返回索引
y=np.searchsorted(arr2,7,side="right")
print(y)