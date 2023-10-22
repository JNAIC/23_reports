def can(numbers_list):
    en = 0
    cn = 0
    for i in numbers_list:
        if i % 2 == 0:          # 偶数
            en += i
        else:
            cn += i
    new_list = [en, cn]
    return new_list


numbers_list = list(map(int, input().split()))

# 打印偶数和奇数的和
print(can(numbers_list))
