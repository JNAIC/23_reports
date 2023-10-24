11111111
def can_form_palindrome(word):
    # 在此处编写你的代码
    from collections import Counter
    counter = Counter(word)
    odd_count = 0
    for count in counter.values():
        if count % 2 !=0:
            odd_count += 1
        if odd_count > 1:
            return False
    return True


# 从用户处获取输入
word = input()
# 调用函数
print(can_form_palindrome(word))

2222222
def check_double_base_palindrome(number):
    # 此处编写代码 

    decimal_str = str(number) 
    binary_str = bin(number)[2:] 
 
    if decimal_str == decimal_str[::-1] and binary_str == binary_str[::-1]:
        return True
    else:
        return False
 
 

# 获取用户输入
number = int(input())

# 调用函数
print(check_double_base_palindrome(number))


33333333333
def list_into_chunks(num_list, chunk_size):    
    # 此处编写代码 
    
    for i in range(0,len(num_list),2):
        
      print(num_list[i.i+2])
# 从用户输入中获取数据，并将其转换为列表
num_list = list(map(int, input().split()))
# 从用户输入中获取块大小
chunk_size = int(input())
# 调用函数
print(list_into_chunks(num_list, chunk_size))


4444444444
def calculate_sum(numbers_list):
    # 此处编写代码 
    a = []
    b = []
    for i in numbers_list:
        if i % 2== 0:
           a.append(i)
        if i % 2 ==1:
            b.append(i)
    s1 = sum(a)  
    s2 = sum(b)
    return[s1,s2]
# 获取输入转为列表
numbers_list = list(map(int,input().split()))

# 打印偶数和奇数的和
print(calculate_sum(numbers_list))


55555555555
def get_unique_elements(nested_tuples):
    # 此处编写代码
    m =[]
    for i in nested_tuples:
        for j in i:
            m.append(j)
    m = list(set(m))
    m.sort()
    return m
# 初始化嵌套元组
nested_tuples = []

# 获取用户输入
for _ in range(3):
    tuple_elements = tuple(map(int, input().split()))
    nested_tuples.append(tuple_elements)

# 调用函数
print(get_unique_elements(nested_tuples))


6666666666
def min_removals_to_anagram(str1, str2):
    # 统计字符出现次数
    list1 = list(str1)
    list2 = list(str2)
    set1 = set(str1)
    set2 = set(str2)
    itst = set1.intersection(set2)
    diff = set1.difference(set2)
    if len(diff) == 0 :
        return 0
    else:
        for i in itst :
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
# 获取输入 
str1 = input()
str2 = input()
 
# 调用函数，输出结果 
print(min_removals_to_anagram(str1, str2))


7777777777
def break_down_list(items):
    # 此处编写代码 
    list0 = []
    for dic in items:
        value = dic["type"]
        n = dic["quantity"]
        dic_new = {"type":value,"quantity":1}
        for i in range(n):
            list0.append(dic_new)
    return list0
# 获取物品列表 
items = eval(input())
# 调用函数，输出分解后的物品列表
print(break_down_list(items))


8888888888
def extreme_words_in_sentence(sentence):
    # 此处编写你的代码 
    l = []
    words = sentence.split()
    max_length = 0
    for word1 in words:
        if len(word1) > max_length:
            max_length = len(word1)
            return max_length
        return word1
        l.append(word1)
    return l
    
    

    min_length = 100
    for word2 in words:
        if len(word2)<min_length:
            min_length = len(word2)
            return min_length
        return word2
        l.append(word2)

    return l 
    print(l.lower())
# 处获取输入
sentence = input()
# 调用函数
print(extreme_words_in_sentence(sentence))