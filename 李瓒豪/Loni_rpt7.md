# 学业压力hin大啊 在搞课内的

# 还有各种演出 在练习和排练

# 学习了神经网络相关内容

# 以下是俱乐部任务的部分代码：

import numpy as np
import pandas as pd
m=97
df=pd.read_excel(r"C:\Users\user\Desktop\workbook1.xlsx")
x0= ones((m,1))
x1= arange((1,m+1)).reshape(m,1)
x= hstack((x0,x1))
y=np.array(df)
a=0.5

def cost_function(theta,X,Y):
    diff=dot(X,theta) - Y
    return(1/(2*m))*dot(diff.transpose(),diff)

def grad(theta,X,Y):
    diff=dot(X,theta)-Y
    return(1/m)*dot(X.transpose(),diff)

def grad_desc(X,Y,alpha):
    theta=array([1,1]).reshape(2,1)
    gradient=grad(theta,X,Y)
    while not all(abs(gradient)<=1e-5):
        the =theta-alpha*gradient
        gradient=grad(theta,X,Y)
    return theta

optimal=grad_desc(X,Y,alpha)
print('optimal:',optimal)  
print('cost_function:',cost_function(optimal,X,Y)[0][0]) 

def plot(X,Y,theta):
    import matplotlib.pyplot as plt
    ax=plt.subplot(111)
    ax.scatter(X,Y,s=30,c='red',marker='s')
    plt.xlabel('X')
    plt.ylabel('Y')
    x=arange(0,21,0.2)
    y=theta[0]+theta[1]*x
    ax.plot(x,y)
    plt.show()

plot(x1,Y,optimal)    

# 下周开始时间稍微有一些了 会慢慢跟上俱乐部的进度 加油！