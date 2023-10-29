import math


def separate(x):
    i = 2
    a = []
    while i <= math.sqrt(x):
        if x % i == 0:
            x /= i
            k = str(i)
            a.append(k)
            continue
        else:
            i += 1
    k = str(int(x))
    a.append(k)
    return ' '.join(a)


n = int(input())
b = 1
str1 = ""
while b <= n:
    x = int(input())
    str1 = str1 + separate(x) + "\n"
    b += 1
print(str1.strip())
