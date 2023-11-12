# 请在 ___ 划线处，替换成你的代码
n = int(input())
t1 = 1
t2 = 1
result = 0

# 循环
while t1 < n:
    # 打印t1
    print(t1)

    # 定义result 为t1和t2之和
    result = t1 + t2

    # 将t2的值分配给t1
    t1 = t2

    # 将result的值分配给t2
    t2 = result
