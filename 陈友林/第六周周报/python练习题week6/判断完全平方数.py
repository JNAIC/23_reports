# 请在 ___ 划线处，替换成你的代码

# 导入math模块
import math

number = int(input())

# 计算平方根
a = math.sqrt(number)

# 对1取余
b = a % 1

# 如果余数等于0，打印"完全平方数"；否则打印"非完全平方数"
if b == 0:
    print("完全平方数")
else:
    print("非完全平方数")
