# 第五周周报

# 最近这几周还是在搞乐队排练的事情 还有 课内的作业和考试啥的 周末会学几课的python内容

# 学了numpy和pandas的一些基础

# 学了epycharts里的一些内容 感觉都是差不多的东西

# 以下是python基础的一些学习过的内容：

## 捕获异常(NameError ZeroDivisionError,Exception )
try:
    print(a)
except:
    a="qweq"
    print(a)    


try:
    print(nmd)
except NameError as n:
    print(n)

try:
    print(1/0)
except (NameError,ZeroDivisionError) as e:
    print(e) 
else:
    print("e")         
finally:
    print("whatever") 

## 模块(可以import模块\类\变量\函数\*,其中*代表该模块所有功能)

### 方法1
import time
print(123)
time.sleep(0.1)
print(234)

import time as t
print(123)
t.sleep(0.1)
print(234)

### 方法2

from time import sleep
print(123)
sleep(0.1)
print(234)

from time import sleep as sl
print(123)
sl(0.1)
print(234)
  

''' 
自定义模块:新建对应模块名的文件夹.py,写入相应功能的函数
两个模块中有相同名的函数,后调用的会覆盖前一个调用的
'''

## main变量(用于模块内部测试 而不影响调用)
if __name__=='__main__':
    print(1)

## __all__和*意思相同

__all__=['test_a']


### from module1 import *



## python包 带有_init_.py的文件的装模块的文件夹

# import my_module1.ad
# ad(1,2)

### from loni_package import module1 的时候,可以将__all__=[]写到_init_文件里 引用*对应的模块



## json数据格式(与python中字典/含有字典的列表 格式相当)
### 转换为json数据格式,即转换为了字符串
import json
data=[{"name":"豆腐干"},{"dfs":1}]
j_str=json.dumps(data)
print(j_str)

### 若要中文 则改为json.dumps(data,ensure_ascii=False)

## json字符串还原为python格式

p=json.loads(j_str)
print(p)

## pyecharts 入门
from pyecharts.charts import Line
from pyecharts.options import TitleOpts,VisualMapOpts,ToolboxOpts,LegendOpts

line=Line()
line.add_xaxis(['china','america','england'])
line.add_yaxis('GDP',[30,20,10])

### 全局配置
line.set_global_opts(
    title_opts=TitleOpts(title="GDP Value",pos_left='center',pos_bottom='1%'),
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True)
)

line.render()

# 下周结束一部分演出和考试之后可能就要开始学神经网络了 包括python的一些刷题也会届时适当地完成
# 加油！！