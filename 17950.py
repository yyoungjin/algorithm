import sys
input = sys.stdin.readline

n, m = map(int, input().split())

res = []
X = 1
for _ in range(n):
    X *= m
    X %= (10**9+7)
    num = int(input())
    res.append(num * X % (10**9+7))
    

print(sum(res) % (10**9+7))


# 큰 수를 다룰 땐 곱셈이 사용된 모든 곳을 잘 확인하자