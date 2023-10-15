# 第二周周报

## 这周去上海有活动就没时间学太多 下周继续!

## 第二周python

## while循环

## 1~100的加和过程

i=0
u=0
while u<=100:
    print(i)
    u+=1
    i+=u

## 猜数字   

# import random
# f=True
# count=0
# num=random.randint(1,200)
# while f:
#     guess=int(input("猜1-200:"))
#     count+=1
#     if guess!=num:
#         if guess>num:
#             print("大了")
#         else:
#             print("小了")
#     else:
#         f=False
# print(f"猜对了,共猜了{count}次")     

# 用while做9*9乘法表
# \t为Tab对齐 ,end=''为不换行

i=1  
while i<=9:
    j=1
    while j<=i:
        print(f"{i}*{j}={i*j}\t",end='')
        j+=1       
    i+=1
    print()




## for语句

for x in range(1,100,2):
    print(x)

### 计数

count=0
for a in "anaconda":
    if a == "a":
        count+=1
print(count)

## range语句

### range(5)
### range(1,5)
### range(1,5,2)

countt=0
r=range(1,100)
for x in r:
    if x%2==0:
        countt+=1
print(countt)    


## continue&break

m=10000
for mem in range(1,21):
    import random
    gpi=random.randint(1,10)
    if gpi<5:
        print("lack of gpi,next")
        continue

    if m>0:
        print("$1000")
        m-=1000
    else:
        print("not enough,bye")
        break
            

## 函数&None（意为False）&函数文档

def add(x,y):
    """
    :param x:数据1
    :param y:数据2
    :return: 结果
    """
    result=x+y
    print(result)
    return result
add(9,8)

nam=None
### 暂时不提供值定义nam
### 函数中变量为局部变量,外部不被定义
### 全局变量global
num=100
def test_a():
    global num
    num=10
    print(num)
test_a()
print(num)    



### practice
money=0
name=input("您的姓名:")
def check(tr):
    if tr:
        print("--------查询余额-------")
    print(f"{name}你好!查询剩余:{money}元")
def save():
    print("---------存款---------")
    saving=int(input("存入:"))
    global money
    money+=saving
    check(False)

def withdraw():
    print("---------取款----------")
    withdrawl=int(input("取出:"))
    global money
    money-=withdrawl
    check(False)

def main():
    print("----------主菜单-----------")
    print(f"{name}你好!请选择操作:")
    print("查询余额\t[输入1]")
    print("存款\t\t[输入2]")
    print("取款\t\t[输入3]")
    print("退出\t\t[输入4]")
    return input("选择操作：")
    _    
while True:
    shuru=main()
    global shuru
    main()
    if shuru=="1":
        check(True)
        continue
    elif shuru=="2":
        save()
        continue
    elif shuru=="3":
        withdraw()
        continue
    elif shuru=="4":
        print("已退出,欢迎下次使用")
        break   


## 列表：[]或list()

nam_list=["tom","list"]
print(nam_list[0],nam_list[-1])
li_list=[[1,2],[3,4]]
print(li_list[0][0])

### 查询下标index

index=nam_list.index("tom")
print(index)

### 修改元素值

nam_list[0]="Tom"
print(nam_list[0])

### 元素插入&追加&删除&统计数量&元素数量统计len

nam_list.insert(0,"tom")

nam_list.append("List")

name_list=[1,2,3]
nam_list.extend(name_list)

print(nam_list)

del nam_list[0]
print(nam_list)

shan=nam_list.pop(1)
print(shan)

nam_list.remove("List")  # 只删除第一个"List"
print(nam_list)

nam_list.clear()
print(nam_list)

print(nam_list.count(2))

print(len(nam_list))

listt=[21,25,21,23,22,20]
listt.append(31)
listtt=[29,33,30]
listt.extend(listtt)
del listt[-1]
print(listt.index(31))
print(listt)


t_list=[1,2,3,4,5,6,7,8,9,10]
for el in t_list:
    if el%2==0:
        print(el)


## 另外学习了神经网络相关内容,诸如偏导/梯度下降/损失函数等原理
## kaggle才刚刚开头 估计下周开始正式看吧
## python基础语法学习了一部分 大概到字典学完内容
## 下周计划:kaggle正式学习/python基础接近尾声/pytorch学习(不过我要乐队排练/学院表演之类的可能会少学)
## 问题:pytorch在外网装装不上啊,科学上网下得太慢了(恼),求救
## so much for rpt week2
