# CreatTime :  2023/10/6 15:15
#数据类型转换
name = '张三'
age = 20

print(type(name),type(age))#name 与 age 数据类型不同
#print('我叫'+name+'今年，'+age+'岁')  #当将str类型与int类型进行连接的时候，报错，解决方案，类型转换
print('我叫'+name+'今年，'+str(age)+'岁')  #把int类型通过str（）函数变成了str类型

a= 10
b= 198.8
c = False

# str（）
print(type(a),type(b),type(c))
print(str(a),str(b),str(c),type(str(a)),type(str(b)),type(str(c)))
#int()  浮点数抹零取整
s1 = '128'
f1 = 98.7
s2 = '76.77'
bo = True
s3 = 'hello'
print(int(s1),type(int(s1))) #将str转换成int，字符串为数字串
print(int(f1),type(int(f1)))#浮点数抹零取整
#print(int(s2),type(int(s2)))#报错，因为是字符串为小数串
print(int(bo),type(int(bo)))#True 当成一了
#print(int(s3),type(int(s3)))#字符串必须为整数

#float()
s1 = '128.98'
s2 = '76'
s3 = 98
bo = True
s4 = 'hello'
print(float(s1),type(float(s1)))
print(float(s2),type(float(s2)))
print(float(s3),type(float(s3)))
print(float(bo),type(float(bo)))
#print(float(s4),type(float(s4))) #非数字串不允许转换



