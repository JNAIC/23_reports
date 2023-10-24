def min_removals_to_anagram(str1, str2):
    # 此处编写代码 
    list1=list(str1)
    list2=list(str2)
    set1=set(str1)
    set2=set(str2)
    set_same=set1.intersection(set2)
    set_difference=set1.difference(set2)
    if len(set_difference) == 0:
        return 0
    else:
        for i in set_same:
            list1.remove(i)
            x=len(list1)
            list2.remove(i)
            y=len(list2)
    return x+y



# 获取输入 
str1 = input()
str2 = input()

# 调用函数，输出结果 
print(min_removals_to_anagram(str1, str2))