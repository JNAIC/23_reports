def get_unique_elements(nested_tuples):
    # 此处编写代码
    numbers=set()
    list_f=[]
    for i in nested_tuples:
        numbers.update(i)
    for j in numbers:
        list_f.append(j)
        list_f.sort()
    return list_f

# 初始化嵌套元组
nested_tuples = []

# 获取用户输入
for _ in range(3):
    tuple_elements = tuple(map(int, input().split()))
    nested_tuples.append(tuple_elements)

# 调用函数
print(get_unique_elements(nested_tuples))