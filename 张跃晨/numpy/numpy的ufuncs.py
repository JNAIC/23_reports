import numpy as np
"""ufunc 用于在 NumPy 中实现矢量化，这比迭代元素要快得多"""
#对两个数组元素相加，方法一：使用zip()
x=[1,3,5,7,9]
y=[2,4,6,8,10]
z=[]
for a,b in zip(x,y):
    z.append(a+b)
print(z)

#方法二：使用ufunc的add()
x=[1,3,5,7,9]
y=[2,4,6,8,10]
z=np.add(x,y)
print(z)