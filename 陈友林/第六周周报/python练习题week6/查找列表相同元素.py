def find_common_elements(list1, list2):
    return sorted(list(set(list1) & set(list2)))

# 获取用户输入，转换为列表


list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

# 调用函数
print(find_common_elements(list1, list2))
