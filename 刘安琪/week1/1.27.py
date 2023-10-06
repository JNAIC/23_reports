n = 1       #n为每次吃完后剩下的桃子数
for i in range(1,10):
    total = (n + 1)*2   #total为每次吃之前已有的桃子总数
    n = total
print(n)
