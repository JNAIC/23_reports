a = eval(input())
b = eval(input())
c = eval(input())
t1 = max(a,b,c)
t3 = min(a,b,c)
t2 = {a,b,c}-{t1,t3}
for t in t2:
    if (t + t3) > t1 and t1 - t < t3 and t1 - t3 < t:
        print(f'{a},{b},{c}能构成三角形的三条边')
    else:
        print(f'{a},{b},{c}不能构成三角形的三条边')
