### 搞了一下线性回归

怎么说呢，原理是懂了一点，但是把理论转换为代码有亿点点困难

这周忙着考试，还有迎新晚会的排练，关于AI的一点没看

呃呃呃，怎么说，感觉要好好学习课内的东西了，要不然期末很难办（期中哭晕在厕所）

import pandas as pd

import numpy as np

import seaborn as sns

data = pd.read_csv('E:/anaconda/test_task/test_task/ex1data1.txt',header = None)



x = data.iloc[:,0]

y = data.iloc[:,1]

sns.regplot(x=x,y=y)



def line_reg(theat,x,b):
    return np.dot(x,theat)+b

def less(y_real,y):
    return ((y_real-y)**2)/2

def update(times,rate,theat,b):

    for time in range (times):
    
        y_real = line_reg(theat,x,b)
        
        theat -= rate*np.sum((y_real-y)*x)/97
        
        b -= rate*np.sum(y_real-y)/97
        
    return theat,b



theat = 1

b = 0.1

rate = 0.015

times = 500

theat,b = update(times,rate,theat,b)

y_real = line_reg(theat,x,b)


sns.regplot(x=x,y=y_real)

sns.regplot(x=x,y=y)
