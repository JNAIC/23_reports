def calculate_sum(numbers_list):
    a = 0
    b = 0
    for i in numbers_list :
        if i % 2 == 0 :
            a += i
        else :
            b += i
    new_list = []
    new_list.append(a)
    new_list.append(b)
    return new_list

numbers_list = list(map(int,input().split()))

print(calculate_sum(numbers_list))