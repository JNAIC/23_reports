1.继续看吴恩达深度学习网课，看到特征缩放部分。

2.开始看神经网络这本书，刚刚看完训练简单的分类器这一部分。

3.完成线性回归那个任务，感觉做了好久，错误很多，不过，好不容易做出来了，感觉最后成本函数值有点大。

代码核心部分，梯度下降的迭代

def grandient_descent(X,Y,alpha):
    w=np.array([1,1]).reshape(2,1)
    grandient=grandient_function(w,X,Y)
    while not all(abs(grandient)<=1e-5):              #all函数，全部成立返回True，否则返回False  abs绝对值函数
        w=w-alpha*grandient
        grandient=grandient_function(w,X,Y)
    return w

optimal=grandient_descent(X,Y,alpha)
print('optimal:',optimal)             #optimal最佳的
print('cost_function:',cost_function(optimal,X,Y)[0][0])