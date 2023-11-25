```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```


```python
fpath = "D:/软件安装/ex1data2.txt"
```


```python
training = pd.read_csv(
fpath,
sep=',',
header=None,
names=['x1','x2','y']
)
```


```python
training
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>x1</th>
      <th>x2</th>
      <th>y</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2104</td>
      <td>3</td>
      <td>399900</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1600</td>
      <td>3</td>
      <td>329900</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2400</td>
      <td>3</td>
      <td>369000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1416</td>
      <td>2</td>
      <td>232000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>3000</td>
      <td>4</td>
      <td>539900</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1985</td>
      <td>4</td>
      <td>299900</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1534</td>
      <td>3</td>
      <td>314900</td>
    </tr>
    <tr>
      <th>7</th>
      <td>1427</td>
      <td>3</td>
      <td>198999</td>
    </tr>
    <tr>
      <th>8</th>
      <td>1380</td>
      <td>3</td>
      <td>212000</td>
    </tr>
    <tr>
      <th>9</th>
      <td>1494</td>
      <td>3</td>
      <td>242500</td>
    </tr>
    <tr>
      <th>10</th>
      <td>1940</td>
      <td>4</td>
      <td>239999</td>
    </tr>
    <tr>
      <th>11</th>
      <td>2000</td>
      <td>3</td>
      <td>347000</td>
    </tr>
    <tr>
      <th>12</th>
      <td>1890</td>
      <td>3</td>
      <td>329999</td>
    </tr>
    <tr>
      <th>13</th>
      <td>4478</td>
      <td>5</td>
      <td>699900</td>
    </tr>
    <tr>
      <th>14</th>
      <td>1268</td>
      <td>3</td>
      <td>259900</td>
    </tr>
    <tr>
      <th>15</th>
      <td>2300</td>
      <td>4</td>
      <td>449900</td>
    </tr>
    <tr>
      <th>16</th>
      <td>1320</td>
      <td>2</td>
      <td>299900</td>
    </tr>
    <tr>
      <th>17</th>
      <td>1236</td>
      <td>3</td>
      <td>199900</td>
    </tr>
    <tr>
      <th>18</th>
      <td>2609</td>
      <td>4</td>
      <td>499998</td>
    </tr>
    <tr>
      <th>19</th>
      <td>3031</td>
      <td>4</td>
      <td>599000</td>
    </tr>
    <tr>
      <th>20</th>
      <td>1767</td>
      <td>3</td>
      <td>252900</td>
    </tr>
    <tr>
      <th>21</th>
      <td>1888</td>
      <td>2</td>
      <td>255000</td>
    </tr>
    <tr>
      <th>22</th>
      <td>1604</td>
      <td>3</td>
      <td>242900</td>
    </tr>
    <tr>
      <th>23</th>
      <td>1962</td>
      <td>4</td>
      <td>259900</td>
    </tr>
    <tr>
      <th>24</th>
      <td>3890</td>
      <td>3</td>
      <td>573900</td>
    </tr>
    <tr>
      <th>25</th>
      <td>1100</td>
      <td>3</td>
      <td>249900</td>
    </tr>
    <tr>
      <th>26</th>
      <td>1458</td>
      <td>3</td>
      <td>464500</td>
    </tr>
    <tr>
      <th>27</th>
      <td>2526</td>
      <td>3</td>
      <td>469000</td>
    </tr>
    <tr>
      <th>28</th>
      <td>2200</td>
      <td>3</td>
      <td>475000</td>
    </tr>
    <tr>
      <th>29</th>
      <td>2637</td>
      <td>3</td>
      <td>299900</td>
    </tr>
    <tr>
      <th>30</th>
      <td>1839</td>
      <td>2</td>
      <td>349900</td>
    </tr>
    <tr>
      <th>31</th>
      <td>1000</td>
      <td>1</td>
      <td>169900</td>
    </tr>
    <tr>
      <th>32</th>
      <td>2040</td>
      <td>4</td>
      <td>314900</td>
    </tr>
    <tr>
      <th>33</th>
      <td>3137</td>
      <td>3</td>
      <td>579900</td>
    </tr>
    <tr>
      <th>34</th>
      <td>1811</td>
      <td>4</td>
      <td>285900</td>
    </tr>
    <tr>
      <th>35</th>
      <td>1437</td>
      <td>3</td>
      <td>249900</td>
    </tr>
    <tr>
      <th>36</th>
      <td>1239</td>
      <td>3</td>
      <td>229900</td>
    </tr>
    <tr>
      <th>37</th>
      <td>2132</td>
      <td>4</td>
      <td>345000</td>
    </tr>
    <tr>
      <th>38</th>
      <td>4215</td>
      <td>4</td>
      <td>549000</td>
    </tr>
    <tr>
      <th>39</th>
      <td>2162</td>
      <td>4</td>
      <td>287000</td>
    </tr>
    <tr>
      <th>40</th>
      <td>1664</td>
      <td>2</td>
      <td>368500</td>
    </tr>
    <tr>
      <th>41</th>
      <td>2238</td>
      <td>3</td>
      <td>329900</td>
    </tr>
    <tr>
      <th>42</th>
      <td>2567</td>
      <td>4</td>
      <td>314000</td>
    </tr>
    <tr>
      <th>43</th>
      <td>1200</td>
      <td>3</td>
      <td>299000</td>
    </tr>
    <tr>
      <th>44</th>
      <td>852</td>
      <td>2</td>
      <td>179900</td>
    </tr>
    <tr>
      <th>45</th>
      <td>1852</td>
      <td>4</td>
      <td>299900</td>
    </tr>
    <tr>
      <th>46</th>
      <td>1203</td>
      <td>3</td>
      <td>239500</td>
    </tr>
  </tbody>
</table>
</div>




```python
m=47
alpha=0.03
max_min_scaler=lambda x:(x-np.average(x))/(np.max(x)-np.min(x))
```


```python
training[['x1']]=training[['x1']].apply(max_min_scaler)
x1=np.array(training['x1']).reshape(m,1)
```


```python
training[['x2']]=training[['x2']].apply(max_min_scaler)
x2=np.array(training['x2']).reshape(m,1)
```


```python
x0=np.ones((m,1))
```


```python
X=np.hstack((x0,x1,x2))
```


```python
X
```




    array([[ 1.00000000e+00,  2.84939738e-02, -4.25531915e-02],
           [ 1.00000000e+00, -1.10502165e-01, -4.25531915e-02],
           [ 1.00000000e+00,  1.10126627e-01, -4.25531915e-02],
           [ 1.00000000e+00, -1.61246787e-01, -2.92553191e-01],
           [ 1.00000000e+00,  2.75598221e-01,  2.07446809e-01],
           [ 1.00000000e+00, -4.32455904e-03,  2.07446809e-01],
           [ 1.00000000e+00, -1.28704041e-01, -4.25531915e-02],
           [ 1.00000000e+00, -1.58213141e-01, -4.25531915e-02],
           [ 1.00000000e+00, -1.71175083e-01, -4.25531915e-02],
           [ 1.00000000e+00, -1.39735480e-01, -4.25531915e-02],
           [ 1.00000000e+00, -1.67349286e-02,  2.07446809e-01],
           [ 1.00000000e+00, -1.87769185e-04, -4.25531915e-02],
           [ 1.00000000e+00, -3.05242281e-02, -4.25531915e-02],
           [ 1.00000000e+00,  6.83209914e-01,  4.57446809e-01],
           [ 1.00000000e+00, -2.02063114e-01, -4.25531915e-02],
           [ 1.00000000e+00,  8.25480278e-02,  2.07446809e-01],
           [ 1.00000000e+00, -1.87722242e-01, -2.92553191e-01],
           [ 1.00000000e+00, -2.10888266e-01, -4.25531915e-02],
           [ 1.00000000e+00,  1.67765899e-01,  2.07446809e-01],
           [ 1.00000000e+00,  2.84147587e-01,  2.07446809e-01],
           [ 1.00000000e+00, -6.44459049e-02, -4.25531915e-02],
           [ 1.00000000e+00, -3.10758001e-02, -2.92553191e-01],
           [ 1.00000000e+00, -1.09399021e-01, -4.25531915e-02],
           [ 1.00000000e+00, -1.06676368e-02,  2.07446809e-01],
           [ 1.00000000e+00,  5.21047752e-01, -4.25531915e-02],
           [ 1.00000000e+00, -2.48395160e-01, -4.25531915e-02],
           [ 1.00000000e+00, -1.49663776e-01, -4.25531915e-02],
           [ 1.00000000e+00,  1.44875662e-01, -4.25531915e-02],
           [ 1.00000000e+00,  5.49694288e-02, -4.25531915e-02],
           [ 1.00000000e+00,  1.75487906e-01, -4.25531915e-02],
           [ 1.00000000e+00, -4.45893136e-02, -2.92553191e-01],
           [ 1.00000000e+00, -2.75973759e-01, -5.42553191e-01],
           [ 1.00000000e+00,  1.08436704e-02,  2.07446809e-01],
           [ 1.00000000e+00,  3.13380902e-01, -4.25531915e-02],
           [ 1.00000000e+00, -5.23113213e-02,  2.07446809e-01],
           [ 1.00000000e+00, -1.55455282e-01, -4.25531915e-02],
           [ 1.00000000e+00, -2.10060908e-01, -4.25531915e-02],
           [ 1.00000000e+00,  3.62159815e-02,  2.07446809e-01],
           [ 1.00000000e+00,  6.10678199e-01,  2.07446809e-01],
           [ 1.00000000e+00,  4.44895612e-02,  2.07446809e-01],
           [ 1.00000000e+00, -9.28518618e-02, -2.92553191e-01],
           [ 1.00000000e+00,  6.54492965e-02, -4.25531915e-02],
           [ 1.00000000e+00,  1.56182887e-01,  2.07446809e-01],
           [ 1.00000000e+00, -2.20816561e-01, -4.25531915e-02],
           [ 1.00000000e+00, -3.16790086e-01, -2.92553191e-01],
           [ 1.00000000e+00, -4.10040957e-02,  2.07446809e-01],
           [ 1.00000000e+00, -2.19989203e-01, -4.25531915e-02]])




```python
Y=np.array(training['y']).reshape(m,1)
```


```python
Y
```




    array([[399900],
           [329900],
           [369000],
           [232000],
           [539900],
           [299900],
           [314900],
           [198999],
           [212000],
           [242500],
           [239999],
           [347000],
           [329999],
           [699900],
           [259900],
           [449900],
           [299900],
           [199900],
           [499998],
           [599000],
           [252900],
           [255000],
           [242900],
           [259900],
           [573900],
           [249900],
           [464500],
           [469000],
           [475000],
           [299900],
           [349900],
           [169900],
           [314900],
           [579900],
           [285900],
           [249900],
           [229900],
           [345000],
           [549000],
           [287000],
           [368500],
           [329900],
           [314000],
           [299000],
           [179900],
           [299900],
           [239500]], dtype=int64)




```python
def cost_function(w,X,Y):
    diff=np.dot(X,w)-Y
    return (1/(2*m))*np.dot(diff.transpose(),diff)
```


```python
def grandient_function(w,X,Y):
    diff=np.dot(X,w)-Y
    return (1/m)*np.dot(X.transpose(),diff)
```


```python
def grandient_descent(X,Y,alpha):
    w=np.array([1,1,1]).reshape(3,1)
    grandient=grandient_function(w,X,Y)
    while not all(abs(grandient)<=1e-5):              #all函数，全部成立返回True，否则返回False  abs绝对值函数
        w=w-alpha*grandient
        grandient=grandient_function(w,X,Y)
    return w

optimal=grandient_descent(X,Y,alpha)
print('optimal:',optimal)             #optimal最佳的
print('cost_function:',cost_function(optimal,X,Y)[0][0])
```

    optimal: [[340412.65957447]
     [504777.90354708]
     [-34952.07588275]]
    cost_function: 2043280050.6028283
    


```python
#绘制散点图
fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
ax.scatter(x1,x2,Y)
X1=np.linspace(-0.5,0.5,20)
X2=np.linspace(-0.5,0.5,20)
y=optimal[0]+optimal[1]*X1+optimal[2]*X2
ax.plot(X1,X2,y,c='r')
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('y')
ax.set_title('3D')
plt.show()
```


    
![png](output_15_0.png)
    



```python

```
