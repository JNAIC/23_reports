#i = eval(input())
#lst = []
#for t in range(2,i):
#    if i%t == 0:
#        if t == 2:
#            lst.append(t)
#        else:
#            for a in range(2,t):
#                if t%a == 0:
#                    break
#                else:
#                    if t not in lst:
#                        lst.append(t)
#print(f'{i}的质数因子是',end="")
#for item in lst:
#    print(f'{item}',end=" ")
#做法错误，注意审题
i = eval(input())
t = 2
while t<=i:
    while i%t == 0:      #不能用if，要用while构成一个循环，才能得到所有值，而非去重
        i = i/t
        print(str(t),end=" ")
    t += 1
