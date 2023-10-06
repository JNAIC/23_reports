#N = eval(input())
#a = 1
#n = 2
#if N == 1 or N == 2:
#    print(f'第{n}个项是1')
#else:
#    if n<=N:
#        n += 1
#        b = a + b
#        print(f'第{n}个项是{b}')
#定义函数，构成递归，很重要
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
print(fib(6))
