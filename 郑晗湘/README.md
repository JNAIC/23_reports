![33ZP(L0_BU5T9%IEMWO_`OE](https://github.com/JNAIC/23_reports/assets/146925826/204968a0-9f93-40b6-bb93-4c7d083713cd)#本周学习

python基本语法及函数https://docs.python.org/zh-cn/3/tutorial/index.html
python题目练习20题
==Python部分题目及了解知识点展示：

```
1.排序
a=int(input('请输入第一个数：'))
b=int(input('请输入第二个数：'))
c=int(input('请输入第三个数：'))
if a<b :
      if a>c :
          print("三个数从小到大为:",c,a,b)
      elif a<c and c<b :
          print("三个数从小到大为:",a,c,b)
      elif a<c and c>b :
          print("三个数从小到大为:",a,b,c)
else :
    if c<b :
       print("三个数从小到大为:",c,b,a)
    elif c>b and a>c :
        print("三个数从小到大为:",b,c,a)
    elif c>b and a<c :

        print("三个数从小到大为:",b,a,c)


list=[a,b,c]
list1=stored(list)
```
2.定义函数
```
def prime(n) :
    flag=True
    for i in range (2,n) :
        if n%i==0 :
            flag= False
            break
    return (flag)
a=int(input('请输入较小数字：'))
b=int(input('请输入第二个较大数字：'))
list=[]
for i in range (a,b+1):
    if prime(i) :
        list.append(i)
print(list)
```    
    
3.格式化
```
    for i in range(1,10):
    print( )
    for j in range (1,i+1):
        print(f'{i}*{j}={i*j}',end=" ")
```




5.
```
a=int(input('请输入一个四位数'))
b=a//1000
c=a%1000//100
d=a%1000%100//10
e=a%1000%100%10

s=e*1000+d*100+c*10+b*1
print(s)
```


6.求阶乘
```
n=4
sum=1
for i in range (1,i+1) ：
      sum*=i
      print(sum)




4.
``       
​    for i in range (100,1000) :
​    a=i%10  #个位#
​    b=i//100
​    c=i%100//10
​    if a**3+b**3+c**3==i :
​        print(i)

```
7.
```
def jiecheng(num) :
   if num==1:
       return 1
else:
        return jiecheng(num-1)*num

```
8.求完数
```
  for i in range (1,1000) :
      sum=0
      for j in range (1,i):
           if i %j==0
           sum+=j
if sum==0
      print(f'{i}')
```

9.字母辨别函数                
a=a.isalpha()辨别字母
10.break的应用
#本周问题
不熟练导致代码复杂
注册不了kaggle暂时使用哔哩哔哩题目


#下周目标
继续练习python语法20题
panda课程

