# CreatTime :  2023/10/6 11:18
#数据类型 int float bool(True False) str(字符串)

#整数类型 整数 负数 0
n1 = 90
n2 = -76
n3 = 0
print(n1 , type(n1))
print(n1 , type(n2))
print(n1 , type(n3))


#整数可以表示为二进制，十进制，八进制，十六进制
print('十进制',118)#默认是十进制
print('二进制',0b1010111)#要在前面加上0b
print('八进制',0o176)#八进制以0o开头
print('十六进制',0x1eaf)#十六进制以0x开头

#浮点数
a = 3.1415926
print(a , type(a))

n1 = 1.1
n2 = 3.2
n3 = 2.1
print(n1 + n2)
print(n1 + n3)#不一定一定存在误差

from decimal import  Decimal
print(Decimal('1.1') + Decimal('3.2'))

#布尔类型
f1 = True
f2 = False
print(f1,type(f1))
print(f2,type(f2))

#布尔值可以转化成整数计算
print(f1 + 1)# 2    1+1  True表示1
print(f2 + 1)# 1    0+1


#字符串类型
str1 = '人参'
str2 = "人参"
str3 = """人
参"""
str4 = '''人
参'''
print(str1,type(str1))








