a,b,c = map(int,input().split(","))
t1 = max(a,b,c)
t2 = min(a,b,c)
t3 = {a,b,c}-{t1,t2}
for t in t3:
    print(t2,t,t1)
