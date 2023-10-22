import numpy as np

"""numpy数组有一个shape的属性"""
arr=np.array([[1,2,3,4,5],[6,7,8,9,0]])
print(arr.shape)
"""结果为（2，5），两个维，每个维5个元素"""


"""ndmin创建不同维度的数组"""
arr2 = np.array([1, 2, 3, 4], ndmin=5)

print(arr2)
print('shape of array :', arr2.shape)
