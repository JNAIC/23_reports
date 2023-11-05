def front3(str1):
    str2 = str1[0:3]
    return f'{str2}{str2}{str2}'


# 输入数据
str1 = eval(input())
# 调用函数打印结果
print(front3(str1))
