## 使用DNArray来处理数据

### 基本运算

   from mxnet import ndarray as nd
   nd.zeros((3,4)) //全为0的矩阵
   x = nd.ones((3,4)) //全为1的矩阵
   x  //相当于print
   nd.array([[1,2],[2,3]])
   y = nd.random_normal(0,1,shape=(3,4)) //均值为0，方差为1，随机生成一个矩阵
   y.shape
   y.size

可以进行加法，指数(nd.exp(y)和矩阵乘法(nd.dot(x,y.T))

### 广播

在进行二元操作时左右两边的ndarray形状不一样时，进行复制操作，使得两边形状相同

   a = nd.arange(3).reshape((3,1))
   b = nd.arange(2).reshape((2,1))
   print('a+b:',a+b)

### 跟NumPy的转换

   import numpy as np
   x = np.ones((2,3))
   y = nd.array(x) // numpy-->mxent
   z = y.asnumpy() // mxent-->numpy
   type(y)

### 操作替换

   x = np.ones((2,3))
   y = np.ones((2,3))
   before = id(y)
   y = y + x
   id(z) == before
out:False //Python默认新建地址并将其复制给y

我们可以通过[:]将结果写到一个之前开好的数组

   z = nd.zeros_like(x)
   before = id(z)
   z[:] = x + y
   id(z) = before
out:True

为了避免开辟空间，可以使用操作符的全名版本中的Out参数

   nd.elemwise_add(x,y,out = z)
   id(z) == before

## 使用autograd自动求导

   import mxent.ndarray as nd
   import mxent.autograd as ag
   x = nd.array([[1,2],[2,3]])
   x.attach_grad() //开辟空间存储导数
   with ag.record():  //定义f,记录求导程序
       y = x*2
       z = y*x
   z.backward() //使用backward求导.如果z不是一个标量，那么其等价于nd.sum(z).backward()
   x.grad //查看求导结果
   x.grad == 4*x
out:[[1. 1.]
     [1. 1.]]

线性回归
   y[i] = 2 * x[i][0] - 3.4 * x[i][1] + 4.2 + noise

## 多层感知机

   import sys
   sys.path.append('..')
   







