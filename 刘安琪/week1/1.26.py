n = 100
count = 0
lst = []
while count<10:
    if count == 0:
        lst.append(n)
        n = n/2
        count += 1
    else:
        lst.append(2*n)
        n = n/2
        count += 1
print(lst[9]/2)
print(sum(lst))
