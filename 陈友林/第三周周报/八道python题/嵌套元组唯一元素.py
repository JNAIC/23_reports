def get_unique_elements(nested_tuples):
    set1 = set()
    list1 = []
    for i in nested_tuples:
        for j in i:
            set1.add(j)            # 利用集合来清除重复的数
    for i in set1:
        list1.append(i)
    list1.sort()
    return list1


# 此处编写代码

# 初始化嵌套元组
nested_tuples = []

# 获取用户输入
for _ in range(3):
    tuple_elements = tuple(map(int, input().split()))
    nested_tuples.append(tuple_elements)

# 调用函数
print(get_unique_elements(nested_tuples))
