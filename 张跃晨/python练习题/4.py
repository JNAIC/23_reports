def calculate_sum(numbers_list):
    # 此处编写代码 
    list_even=[]
    list_odd=[]
    result1=0
    result2=0
    for i in numbers_list:
        if i%2 == 0:
            list_even.append(i)
            result1=sum(list_even)
        else:
            list_odd.append(i)
            result2=sum(list_odd)
    list_final=[result1,result2]
    return list_final

# 获取输入转为列表
numbers_list = list(map(int,input().split()))

# 打印偶数和奇数的和
print(calculate_sum(numbers_list))