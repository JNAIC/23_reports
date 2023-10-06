a,b = map(int,input().split(","))
lst = []
for i in range(a,b+1):
    for t in range(2,i):
        if i % t == 0:
            break
        else:
            lst.append(i)
            break
print(lst)
