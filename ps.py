# 2003
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

ep = 0
num = arr[0]
count = 0
for sp in range(n):
    while num < m and ep < n-1:
        ep += 1
        num += arr[ep]
    if num == m:
        count += 1

    num -= arr[sp]

print(count)