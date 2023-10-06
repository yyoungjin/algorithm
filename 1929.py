# 애라토스테네스의 채

m, n = map(int, input().split())

primes = [True] * (n + 1)
primes[0], primes[1], primes[2] = False, False, True

p = 2
while p ** 2 <= n:
    if primes[p]:
        for i in range(p**2, n+1, p):
            primes[i] = False

    p += 1

res = [print(i) for i in range(m, n+1) if primes[i]]
