#海伦公式 p = (a+b+c)/2 s=sqrt(p(p-a)(p-b)(p-c))
from math import*
a = eval(input())
b = eval(input())
c = eval(input())
p = (a + b + c)/2
s = sqrt(p*(p-a)*(p-b)*(p-c))
print(s)
