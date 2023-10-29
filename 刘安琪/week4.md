A 三位数排序

```python
s = input()
s = s.split()
s.sort()
for i in s:
    print(i,end = " ")
```

这道题，原先split用法错了，应该是split()，而不是split(" ")。

C 输入字符菱形

```python
print("  *  ")
print(" *** ")
print("*****")
print(" *** ")
print("  *  ")
```

我的代码好像跟现在写的一模一样，不知道为什么是compile error，有可能是我没选语言，然后给我自动识别成了C++

D 最长最短单词

```python
def fun(x):
    x=x.replace(',',' ')
    x=x.replace('.',' ')
    x=x.split()
    m = max(x,key = len)
    n = min(x,key = len)
    t = (m,n)
    return t
s = input()
s1 = fun(s)
for i in s1:
    print(i)
```

之前没有把除空格外的分隔符替换，直接以空格分隔，导致结果错误

F 【模板】排序

```python
s = []
for i in range(2):
    s += input().split()
s.sort()
print(' '.join(str(i) for i in s))
print()
```

我在自己的编译器上运行没有问题，但是在交的时候一直不对，我也不知道是什么问题，多行输入如何输入，for循环

G 分解质因子

```python
i = eval(input())
for s in range(i):
    n = eval(input())
    lst1 = []
    for t in range(2,n+1):
        if n%t == 0:
            count = 0
            for m in range(2,t+1):
                if t%m == 0:
                    count += 1
            if count <= 2:
                lst1.append(t)
    for p in lst1:
        print(p,end=" ")
        
```

代码不对，但是我不知道为什么不对，输入不太会输入，后面的分解质因子，我感觉是这样做。

H 谁拿了最多奖学金

```python
n1 = eval(input())
dict2 = {}
sum1 = 0
for i in range(n1):
    s = list(map(int,input().split()))
    dict1 = {}
    dict1[s[0]] = [s[1],s[2],s[3],s[4],s[5]]
    money = 0
    if dict1[s[0]][0] > 80 and dict1[s[0]][4] >= 1:
        money += 8000
    if dict1[s[0]][0] > 85 and dict1[s[0]][1] > 80:
        money += 4000
    if dict1[s[0]][0] > 90:
        money += 2000
    if dict1[s[0]][0] > 85 and dict1[s[0]][3] == 'Y':
        money += 1000
    if dict1[s[0]][1] > 85 and dict1[s[0]][2] == 'Y':
        money += 850
    sum1 += money
    dict2[s[0]] = money
lst = [(k,v) for v,k in dict2.items()]
lst.sort()
print(lst[0][1])
print(lst[0][0])
print(sum1)
```

尝试着写，也不会



这周开始的那个吴恩达深度学习，第一个文件的读写就不行，一直显示unable to open，然后看网上教程，把文件拷到jupyter文件里面，好不容易解决之后，又因为文件路径里的\ ，涉及转义字符，又查了之后，在文件路径前加了个r，保持路径原样之后，才勉强没有报错。这个第一步就花费了很久，，，
