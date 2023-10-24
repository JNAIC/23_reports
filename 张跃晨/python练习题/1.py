def can_form_palindrome(word):
    # 在此处编写你的代码
    set_str=set(word)
    if len(word)%2 == 0:
        if len(word)/2 == len(set_str):
            return True
        else:
            return False
    else:
        if (len(word)+1)/2 == len(set_str):
            return True
        else:
            return False
# 从用户处获取输入
word = input()
# 调用函数
print(can_form_palindrome(word))