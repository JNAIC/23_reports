import numpy as np

"""使用reshape()将数组重塑"""
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
print(newarr)
"""从左向右的索引即numpy数组从外向内，三维也相同"""
"""返回的数组是一个视图"""

"""可以传递-1作为未知的维度，但-1仅能存在一下"""

arr2 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr2.reshape(2, 2, -1)
print(newarr)

"""展平数组，将多维转化为一维，使用reshape(-1)"""
arr3= np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr3.reshape(-1)
print(newarr)