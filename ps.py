# 1644
def sieve_of_eratosthenes(n):
    primes = [True] * (n+1)  # 0부터 n까지의 모든 수를 포함하는 리스트 생성, 초기값은 모두 소수로 가정

    primes[0], primes[1] = False, False  # 0과 1은 소수가 아니므로 False로 설정

    p = 2
    while p * p <= n:
        if primes[p] == True:  # p가 소수인 경우
            for i in range(p * p, n + 1, p):
                primes[i] = False  # p의 배수들을 모두 소수가 아닌 것으로 표시

        p += 1

    prime_numbers = [num for num in range(n+1) if primes[num]]  # 소수들을 리스트에 저장
    return prime_numbers

n = int(input())
arr = sieve_of_eratosthenes(n)

ep = 0
if not arr:
    print(0)
    exit()
num = arr[0]
count = 0
for sp in range(len(arr)):
    while num < n and ep < (len(arr)-1):
        ep += 1
        num += arr[ep]
    
    if num == n:
        count += 1
    
    num -= arr[sp]

print(count)