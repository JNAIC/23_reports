def separate(x):
    i = 2
    a = []
    while i <= 3:
        if x % i == 0:
            x /= i
            k = str(i)
            a.append(k)
            continue
        else:
            i += 1
    if x == 1:
        return ' '.join(a)
    else:
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
