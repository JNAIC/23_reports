import math


def check_perfect(num):
    i = 2
    j = 1
    while i <= math.sqrt(num):
        if num % i == 0:
            j += i
            k = num / i
            j += k
            i += 1
        else:
            i += 1
    if j == num:
        return True
    else:
        return False


# 输入处理
num = int(input())

# 调用函数
print(check_perfect(num))
