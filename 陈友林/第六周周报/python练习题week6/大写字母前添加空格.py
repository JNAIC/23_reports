def add_space_before_capital(word):
    result = ""
    for char in word:
        if char.isupper():
            result = result + " " + char
        else:
            result += char
    result = result.lower()
    return result
# 获取用户输入


word = input()

# 调用函数
print(add_space_before_capital(word))
