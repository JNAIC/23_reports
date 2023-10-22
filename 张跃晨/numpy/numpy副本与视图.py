import numpy as np

"""copy()为副本，view()为视图
   副本有数据，视图无数据"""
arr=np.array([1,2,3,4,5])
x=arr.copy()
x[1]=10
print(arr)
print(x)

y=arr.view()
y[1]=10
print(arr)
print(y)

"""检查数组是否具有数据,使用属性base"""
arr=np.array([1,2,3,4,5])
x=arr.copy()
y=arr.view()
print(x.base)
print(y.base)