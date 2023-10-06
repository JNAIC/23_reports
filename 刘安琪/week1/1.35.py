a = []
sum = 0
for i in range(3):
    a.append([])
    for j in range(3):
        k = eval(input())
        a[i].append(k)
        if i == j:
            sum += a[i][j]
print(a)
print(sum)
