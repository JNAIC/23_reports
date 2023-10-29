# 这周基本上都在乐队排练和演出还有作业,抽空学了点python基础,下周继续!
# 基于上周例会的测试,浅浅做了几道python题目巩固了一下


# 以下是第四周python:

## 修改更新字典tip
dic1={"林":{"j":1},"网":{"j":2},"张":{"j":3}}
for name in dic1:
    if dic1[name]["j"]==1:
        e_info=dic1[name]
        e_info["j"]+=100
        dic1[name]=e_info
print(dic1)        


## 函数参数

### 位置参数
### 关键字参数（name=Loni的键值对形式，可以不对应顺序;可以和位置参数混用,但位置参数要在最前面）

def user_info(name,age,gender):
    print(f"{name},{age},{gender}")
user_info("LONI",20,gender="male")   

### 缺省参数(默认值)(默认值必须在最后)

def user_info(name,age,gender="male"):
    print(f"{name},{age},{gender}")
user_info("LONI",20)   

### 不定长参数

#### 位置不定长(形成元组)
def us_info(*args):
    print(args)

us_info("t","l",87)

#### 关键字传递(形成字典)

def use_info(**kwargs):
    print(kwargs)

use_info(name="Lon",age=2,id=123)

### 函数作为参数传递

def tes_func(compute):
    result=compute(1,2)
    print(result)
def compute(x,y):
    return x+y    
tes_func(compute)


### lambda匿名函数(无名称,临时使用一次,只能写一行)

tes_func(lambda x,y:x+y)

## 文件编码(UTF-8,GBK,Big5等)
## 文件读取(encoding位置不是第三位,不用位置参数,而用关键字参数指定)

### r-只读,w-写入,打开文件从头编辑并覆盖/创建新文件,a-打开并追加新内容/创建新文件
f=open('D:/python.txt','r',encoding="UTF-8")

### 文件操作()

#### 读取数据内容,以字节为单位,没有输入则全部读取
##### !!!打开文件后没关闭,则读取文件会续接上一次读取点

print(f.read(12))

#### 读取一行

print(f.readline())

#### 读取文件全部行,封装到列表中
#### \n为回车换行符

print(f.readlines())

#### for循环读取每一行数据

for x in f:
    print(x)

#### 关闭文件占用

f.close()

#### 自动对文件close

with open("D:/python.txt","r",encoding="UTF-8") as f:
    for line in f:
        print(line)

#### 文件写入
#### write只是写在程序的内存(缓冲区)里,调用flush/close时内容才真正写入文件 

f=open("D:/python.txt","a",encoding="UTF-8")
f.write("Hello World")

f.flush()
f.close()

#### line.strip()来去除每一行空格和换行符
