# CreatTime :  2023/10/6 16:03
#输入函数input

'''
present= input('想要什么礼物呢')
print(present,type(present))#输出为str类型


num1 = int(input('请输入第一个数字'))
#num1 = int(num1) 将转换后的结果以int储存到num1中
num2 = int(input('请输入第二个数字'))
print(num1 + num2)

# 一正一负整除
print(9 // -4)
print(-9 // 4)#向下取整数

print(9 % -4)#余数=被除数-除数*商(被除数/除数)
'''

#赋值运算符
i = 3+4
print(i)

#链式赋值
a=b=c=20
print(a,id(a))
print(b,id(b))
print(c,id(c))

print('--------支持参数赋值--------')
a = 20
a += 30
print(a)
print(type(a))
a -= 10
a *= 2
print(a)
print(type(a))
a /= 3
print(a)
print(type(a))#此时a的类型变了
a //= 2
print(a)


#解包赋值
a,b,c = 20,30,40
print(a,b,c)
print('-----交换两个变量的值-----')
a,b = 10,20
print('交换之前：',a,b)
a,b = b,a
print('交换之后：',a,b)


#**比较运算符，比较运算结果为bool类型
a,b = 10,20
print(a < b)
print(a > b)
print(a == b)
print(a <= b)
print(a >= b)
print(a != b)
'''一个 = 称为赋值运算符， == 称为比较运算符
一个变量有表示，类型，值组成
== 比较的是value
比较对象的标识使用的是 is
'''
a = 10
b = 10
print(a == b)# a与b value 相等
print(a is b) #True a与b id 相等
print(id(a))
print(id(b))
#没学，抄
list1 = [11,22,33,44]
list2 = [11,22,33,44]
print(list1 == list2)
print(list1 is list2)
print(list1 is not list2)


#**bool运算符
# and 并且 有一个为false,结果为false
# or 或者 有一个为true,结果为true

#not True
print(not True)
#not False
print(not False)

#in //mot in
s = 'helloworld'
print('w' in s)
print('k' not in s)
'''in(判断表达式的值是否位于给出的列表中，
如果是返回true，
或者返回false) 
not in（判断表达式的值是否不位于给出的列表中，
如果不是返回true，
或者返回false）'''

#**位运算符，将数据转化为二进制进行运算

# 位与&，同为一时结果为一
print(4 & 8)
#位或|，同为0时结果为0
print(4 | 8)
#  左移1位，相当于*2
#右移位，高位补0，低位截断，相当于/2
print(6 << 2)
print(6 >> 3)#相当于6//8 = 0

#**运算符的优先级
#括号>算数> 位 >比较> 布尔 >赋值
