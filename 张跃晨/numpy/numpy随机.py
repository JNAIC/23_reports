import numpy as np
#numpy中含有生成随机数的模块
from numpy import random
"""用randint()例如随机生成0-100的随机数"""
x=random.randint(100)
print(x)
print("\n")

"""用rand()生成随机浮点数"""
y=random.rand()
print(y)
print("\n")

"""生成随机数组"""
#生成一维数组，包含5个从1-100的随机数
a=random.randint(100,size=(5))
print(a)
print("\n")
#生成有三行的二维数组，每行包含5个1-100的随机数
b=random.randint(100,size=(3,5))
print(b)
print("\n")
#生成有三行的二维数组，每行包含5个1-100的随机浮点数
c=random.rand(3,5)
print(c)
print("\n")

"""使用方法choice()从数组中生成随机数"""
m=random.choice([1,3,5,7,9])
print(m)
print("\n")
#可以使用size指定数组的形状
n=random.choice([1,2,3,4,5,6,7,8,9],size=(4,3))
print(n)