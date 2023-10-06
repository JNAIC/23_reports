n = eval(input())
n = str(n)
a = n[::-1]
if a == n:
    print(f'{n}是回文数')
else:
    print(f'{n}不是回文数')
