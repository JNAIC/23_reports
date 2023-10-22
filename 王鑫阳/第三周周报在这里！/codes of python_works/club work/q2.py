def check_plindrome(num) :
    length = len(str(num))
    NUM = str(num)
    for i in range(length // 2) :
        if NUM[i] != NUM[length - i - 1] :
            return 0
    return 1

def check_double_base_plindrome(number) :
    bin_num = bin(number)[2:]
    a = check_plindrome(number)
    b = check_plindrome(bin_num)
    if a+b == 2 :
        return "True"
    else :
        return "False"

number = int(input())
print(check_double_base_plindrome(number))