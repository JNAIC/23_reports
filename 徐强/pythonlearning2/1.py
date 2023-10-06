# CreatTime :  2023/10/4 21:31
#二进制语言与字符编码
import keyword

print(chr(0b100111001011000))
print(ord('乘'))


#python中的保留字，不能够用来命名
print(keyword.kwlist)


#变量的定义和使用
name = '玛丽亚'
print(name)
#变量的三个组成部分1.标识id2.类型type3.值value
print('表示',id(name))
print('类型',type(name))
print('值',name)#name 里面存储的是290093.....指向标号为2900....的变量


#多次赋值之后，变量名会指向新的空间






