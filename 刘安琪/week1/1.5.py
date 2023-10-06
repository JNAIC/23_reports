m = eval(input())
if m == 0:
    s = 1
else:
    s = 1
    for i in range(1,m + 1):
        s = s * i
        i += 1
print("{}!={}".format(m, s))
