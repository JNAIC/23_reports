# 完成下面的函数

# 定义函数
def is_palindrome(string):
    string1 = string.replace(" ", "")
    string2 = string1.replace(",", "")
    string3 = string2.replace(":", "")
    str1 = string3.lower()
    str2 = str1[::-1]
    if str1 == str2:
        return True
    else:
        return False


string = input()
result = is_palindrome(string)
print(result)
