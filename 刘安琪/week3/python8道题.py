#第一题
def can_form_palindrome(word):
    # 在此处编写你的代码
    lst = []
    for i in word:
        s = word.count(i)
        lst.append(s)
    count = 0
    for i in lst:
        if i % 2 != 0:
            count += 1
    if count <= 1:
        return True
    else:
        return False

# 从用户处获取输入
word = input()
# 调用函数
print(can_form_palindrome(word))


#第二题
def check_double_base_palindrome(number):
    # 此处编写代码 
    number = str(number)
    if number == number[::-1]:
        number = int(number)
        number = bin(number)[2:]
        number = str(number)
        if number == number[::-1]:
            return True
    return False


# 获取用户输入
number = int(input())

# 调用函数
print(check_double_base_palindrome(number))


#第三题
def list_into_chunks(num_list, chunk_size):    
    # 此处编写代码 
    lst = []
    for i in range(0,len(num_list),chunk_size):
        s = num_list[i:i+chunk_size]
        lst.append(s)
    return lst
    
# 从用户输入中获取数据，并将其转换为列表
num_list = list(map(int, input().split()))
# 从用户输入中获取块大小
chunk_size = int(input())
# 调用函数
print(list_into_chunks(num_list, chunk_size))


#第四题
def calculate_sum(numbers_list):
    # 此处编写代码 
    lst = []
    even_sum = 0
    odd_sum = 0
    for i in numbers_list:
        if i % 2 == 0:
            even_sum += i
        else:
            odd_sum += i
    lst.append(even_sum)
    lst.append(odd_sum)
    return lst
# 获取输入转为列表
numbers_list = list(map(int,input().split()))

# 打印偶数和奇数的和
print(calculate_sum(numbers_list))


#第五题
def get_unique_elements(nested_tuples):
    # 此处编写代码
    lst = []
    for i in nested_tuples:
        for j in i:
            if j not in lst:
                lst.append(j)
    lst.sort()
    return lst

# 初始化嵌套元组
nested_tuples = []

# 获取用户输入
for _ in range(3):
    tuple_elements = tuple(map(int, input().split()))
    nested_tuples.append(tuple_elements)

# 调用函数
print(get_unique_elements(nested_tuples))


#第六题
def min_removals_to_anagram(str1, str2):
    # 此处编写代码 
    dic1 = {}
    for i in str1:
        if i in dic1:
            dic1[i] += 1
        else:
            dic1[i] = 1
    s = 0
    for i in str2:
        if i in dic1 and dic1[i] > 0:
            dic1[i] -= 1
            if dic1[i] == 0:
                del dic1[i]
        else:
            s += 1
    for i in dic1:
        s += dic1[i]
    return s

# 获取输入 
str1 = input()
str2 = input()

# 调用函数，输出结果 
print(min_removals_to_anagram(str1, str2))


#第七题
def break_down_list(items):
    # 此处编写代码 
    lst = []
    for i in items:
        if i['quantity'] == 0:
            lst = []
        else:
            s = i['quantity']
            if s>1:
                i['quantity'] = 1
                for t in range(s):
                    lst.append(i)
            else:
                lst.append(i)
    return lst

# 获取物品列表 
items = eval(input())
# 调用函数，输出分解后的物品列表
print(break_down_list(items))


#第八题
def extreme_words_in_sentence(sentence):
    # 此处编写你的代码
    sentence = sentence.lower()
    sentence = sentence.split()
    m = max(sentence,key = len)
    n = min(sentence,key = len)
    t = (m,n)
    return t


# 处获取输入
sentence = input()
# 调用函数
print(extreme_words_in_sentence(sentence))
