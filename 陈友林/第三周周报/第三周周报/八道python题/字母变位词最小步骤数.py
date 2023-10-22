def min_removals_to_anagram(str1, str2):
    j = 0
    for i in str1:
        if str2.count(i) != 0:
            str1 = str1.replace(i, "", 1)     # 特别注意，此处i为字符串！！！！！！！
            str2 = str2.replace(i, "", 1)
    length_str1 = len(str1)
    length_str2 = len(str2)
    a = length_str1 + length_str2
    return a


# 获取输入
str1 = input()
str2 = input()

# 调用函数，输出结果
print(min_removals_to_anagram(str1, str2))