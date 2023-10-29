def allin(element):
    return int(element)             # 注意要将列表中的字符串类型转换为int类型，否则无法比较大的数据


n = int(input())
s1 = input()
list1 = s1.split()
list1.sort(key=allin)
print(' '.join(list1))

