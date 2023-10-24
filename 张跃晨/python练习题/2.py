def check_double_base_palindrome(number):
    # 此处编写代码
    left1=str(number)
    right1=left1[::-1]
    bin_number=int(bin(number)[2:])
    left2=str(bin_number)
    right2=left2[::-1]
    if left1 == right1:
        if left2 == right2:
            return True
        else:
            return False
    else:
        return False
    

# 获取用户输入
number = int(input())

# 调用函数
print(check_double_base_palindrome(number))