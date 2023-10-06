# 第一次周报倾心奉上

## 树树是神!!

### 国庆写了高数作业和工程制图!!!

$$
\lim_{x\to\infin}\frac{sin(t)}{x}=1
$$

### 还有python的一些初等学习!

(国庆在忙乐队排练,学的python比较少,树树会原谅我的对吧!!)

### 以下呈上随便练的代码:

#### 输入

print("树树是神!!!")

#### 运算符及数据类型
print(type(int("11")),int("11"))
a=int("11")
print(type(a))
type_int=int(13.14)
print(type(type_int),type_int)
print("13*5=",13*5)
print("13/6=",13//6)
print(13%6)
print(13**6)
num=13**6%32
print(num)
numm="11"
print(numm)
name="\'jnuer\'"
print(name)
print(name+numm)

#### 字符拼接用%或+

zb1="不想写:%s和%s" % ("周报","工程制图作业")
print(zb1)

#### 格式化及占位符

name="loni"
setup_y=0o3
parc=2.0
print("名为%s,初始化于%d,现有%f" % (name,setup_y,parc))

##快速格式化(无精度):f(format)
print(f"名为{name},初始化于{setup_y},现有{parc}")

#### 精度控制(小数点及小数后均计入位数)
num1=114514
num2=114.514
print("num1宽度限制为7:%7d" % num1)
print("num2宽度限制为8,精确到2位:%8.2f" % num2)
print("num2不限制宽度,精确到3位:%.3f" % num2)

#### 字符串格式化练习

name="tx"
stock_price=19.99
stock_code="003032"
d_growth_factor=1.2
growth_days=7
final_pr=stock_price*d_growth_factor**growth_days
print(f"公司:{name},股票代码:{stock_code},当前股价:{stock_price},日增长系数为:{d_growth_factor},经过{growth_days}天,股价达到了:{final_pr}")
 
#### 数据输入(input)

test=input("请大声告诉我谁是神!!!")
print("没错,我也认为%s是神!! " % test) 

##练习

user_name=input("您的用户名称为:")
user_type=input("您的用户类型为")
print("您好:%s,您是尊贵的%s用户,欢迎您的光临!" %(user_name,user_type))

#### 布尔/比较 (==,!=,>,<,>=,<=)

num11=114
num22=514
print(f"{num11 != num22}")
print(f"114大于514吗:{num11>=num22}")

#### 判断语句(4个空格缩进)

##### if语句

jnaic=233333
if jnaic >=114514:
    print("树树是神!")
    print("树树唯一真神!")

##### else语句

if jnaic == 1145141:
    print("树树真是神吗???")
else:
    print("树树真是神!") 

##### elif语句    (elif之间互斥)

num114=int(114514)
input("猜猜我心里想的数字是什么:")
if input == num114:
    print("nb!!!!")   
elif int(input("戳啦,再猜"))==num114:
    print("nb!!!!")
elif int(input("再猜一次"))==num114:
    print("nb!!!!!")
else:
    input("戳啦,是114514")
       
#### 判断语句嵌套

print("欢迎来到jnaic")
if int(input("请输入您的身高"))>200:
    print("你这身高还不去打篮球!!!")
    print("对个暗号吧!!")

    if int(input("树树是神吗!! 1是0不是"))==int(1):
        print("暗号正确!!!")
    else:
        print("树树就是神!!!")    
else:
    print("欢迎来到jnaic")
          
### 学了kaggle入门(几乎没学)

### 学了vscode和markdown的一些基本语法和用法

### 名字不是"豪"是"壕"啊!!!我也不知道为啥起这么复杂

### 树树是神!!!(例会要点察觉)

### 下周计划：
python：while，for语法及函数、列表、字典等
kaggle：pandas等相关内容
视觉神经网络浅了解

### 周报到此！！ 树树是神！！