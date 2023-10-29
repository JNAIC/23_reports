import math

def isprime(K):
    if K <= 1:
        return False
    k = int(math.sqrt(K))
    for m in range(2,k+1):
        if K % m == 0:
            return False
    return True

def primes(n):
    primesx = []
    i = 2
    while i <= n:
        if n % i == 0:
            if isprime(i):
                primesx.append(i)
                n = n // i
            else:
                for j in range(2, int(math.sqrt(i)) + 1):
                    if i % j == 0 and isprime(j):
                        primesx.append(j)
                        i = i // j
                        break
        else:
            i += 1
    return primesx

T = int(input())
for _ in range(T):
    X = int(input())
    ans = primes(X)
    print(" ".join(map(str,ans)))