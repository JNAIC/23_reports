a = []
for i in range(10):
    a.append([])
    for j in range(10):
        a[i].append(0)
for i in range(10):
    a[i][0] = 1
    a[i][i] = 1
for i in range(2,10):
    for j in range(1,10):
        a[i][j] = a[i-1][j] + a[i-1][j-1]
for i in range(10):
    for j in range(i+1):
        print(a[i][j],end=" ")
    print()
