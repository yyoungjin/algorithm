# 1806
import sys
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))

INF = 1e5

ep = 0
num = arr[0]
size = INF
for sp in range(n):
    while num < s and ep < n-1:
        ep += 1
        num += arr[ep]

    if num >= s:
        size = min(size, (ep - sp + 1))
    
    num -= arr[sp]

if size == INF:
    print(0)
else:
    print(size)