import numpy as np
"""过滤：从原有数组中取出一些数据构成新的数组，使用布尔索引列表"""
arr = np.array([61, 62, 63, 64, 65])
x=[True,False,True,False,True]
new_arr=arr[x]
print(new_arr)
print("\n")

"""创建过滤器数组"""
arr2 = np.array([61, 62, 63, 64, 65])
#过滤出大于62的数字

#创建一个空的列表
list=[]
#遍历arr2中的元素
for i in arr2:
    if i >=62:
        j=True
    else:
        j=False
    list.append(j)
new_arr2=arr2[list]
print(new_arr2)
print("\n")

"""直接从数组创建过滤器"""
arr2 = np.array([61, 62, 63, 64, 65])
index_arr=(arr2>=62)
new_arr3=arr2[index_arr]
print(new_arr3)
