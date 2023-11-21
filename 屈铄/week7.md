1. 看吴恩达深度学习网课

2. 完成线性回归那个任务，感觉做了好久，错误很多（这两周比较忙没怎么改）

   代码核心部分（梯度下降）

```python
def cost_function(theta, X, Y):
    diff = dot(X, theta) - Y
    return (1/(2*m)) * dot(diff.transpose(), diff)
def gradient_function(theta, X, Y):
    diff = dot(X, theta) - Y
    return (1/m) * dot(X.transpose(), diff)
def gradient_descent(X, Y, alpha):
    theta = array([1, 1]).reshape(2, 1)
    gradient = gradient_function(theta, X, Y)
    while not all(abs(gradient) <= 1e-5):
        theta = theta - alpha * gradient
        gradient = gradient_function(theta, X, Y)
    return theta
```

3.期中已经人麻了，感觉要先搞课内了