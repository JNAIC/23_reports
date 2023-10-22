import numpy as np
"""使用sort()函数对数组进行排序"""
arr = np.array([3, 2, 0, 1])
new_arr=np.sort(arr)
print(new_arr)
print("\n")
#此方法返回数组的副本，而原始数组保持不变。
#对字母，布尔数组均可实现排列

"""对二维数组进行排列"""
arr2 = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arr2))