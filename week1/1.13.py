for i in range(100,1000):
    t1 = i//100
    t2 = (i-t1*100)//10
    t3 = i-t1*100-t2*10
    if i == t1*t1*t1 + t2*t2*t2 + t3*t3*t3:
        print("{}是水仙花数".format(i))
