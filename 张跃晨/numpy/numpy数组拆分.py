import numpy as np
"""使用arr_split()对较短数组进行拆分"""
arr = np.array([1, 2, 3, 4, 5, 6])
print(np.array_split((arr),4))
print("\n")

"""拆分为数组后可以像访问数组元素那样访问它们,在其后面加索引即可"""
arr = np.array([1, 2, 3, 4, 5, 6])
new_array=np.array_split((arr),4)
print(new_array[2])
print("\n")

"""使用hsplit()按照行拆分数组 """
arr2= np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
new_array2=np.hsplit((arr2),3)
print(new_array2)
print("\n")

"""使用vsplit()按照列进行拆分"""
arr2= np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
new_array3=np.vsplit((arr2),3)
print(new_array3)