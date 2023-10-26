def power(a, b, c):
    if b == 0:
        return 1
    elif b%2 == 0: # 짝수인 경우
        half_pow = power(a, b//2, c)
        return (half_pow * half_pow) % c
    else:
        half_pow = power(a, (b-1) // 2, c)
        return (a * half_pow * half_pow) % c
    
a, b, c = map(int, input().split())
print(power(a, b, c))