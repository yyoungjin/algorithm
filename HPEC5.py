
# 모듈러 지수 함수
def mod_pow(n, k, mod):
    result = 1
    
    n %= mod
    if n == 0:
        return 0
    
    while k > 0:
        if k % 2 == 1:
            result = (result * n) % mod
        k //= 2
        n = (n * n) % mod
    
    return result


# result = mod_pow(3, 3, 7)
# print(result)



mod = 1000000007

p, c, k = map(int, input().split())
k -= 1

m = list(map(int, input().split()))

if p == 1:
    print("-1")
else:
    d = [m[i + 1] - m[i] for i in range(p - 1)]
    d.append(0)

    for j in range(1, p):
        d[p - 1] -= mod_pow(c, j, mod) * d[p - 1 - j]

    answer = mod_pow(c, (k // p) * p, mod) * abs(d[k % p]) % mod
    print((answer + mod) % mod)