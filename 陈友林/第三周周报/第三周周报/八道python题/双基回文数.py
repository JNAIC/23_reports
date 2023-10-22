def can(number):

    s = str(number)
    b = s[::-1]         # 将number转换为字符串并用切片方法进行颠倒操作
    a = ""
    while number != 0:
        a = str(number % 2) + a     # 将number转换为二进制
        number //= 2
        c = a[::-1]      # 将二进制数颠倒
    if int(s) == int(b) and a == c:     # 通过是否相等判断是否为回文
        return True
    else:
        return False


number = int(input())
print(can(number))