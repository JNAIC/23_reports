for i in range(1,1000):
    s = 0
    for t in range(1,i):
        if i%t == 0:
            s = s + t
    if s == i:
        print(f'{i}是完数')
