def jie(n):
    if n == 1:
        return 1
    else:
        return n*jie(n-1)
s = jie(1)+jie(2)+jie(3)+jie(4)+jie(5)+jie(6)+jie(7)+jie(8)+jie(9)+jie(10)+jie(11)+jie(12)+jie(13)+jie(14)+jie(15)+jie(16)+jie(17)+jie(18)+jie(19)+jie(20)
print(s)
#引用math库
#import math
#sum = 0
#for i in range(1,21):
#sum += math.factorial(i)
#print(sum)
