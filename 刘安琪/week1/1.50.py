def func(a,b):
    if a == b:
        return a
    num = min(a,b)
    while a%num != 0 or b%num != 0:
        num -= 1
    return num
print(func(12,18))
