# 请在 ___ 划线处，替换成你的代码

# 创建函数，参数为可变数量的参数
def multiply_numbers(*n):
    j = 1
    for i in n:
        j *= i
    return j

# 输入三个整数


n1 = int(input())
n2 = int(input())
n3 = int(input())

# 调用函数
result = multiply_numbers(n1, n2, n3)

# 打印结果
print(result)
