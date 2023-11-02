# 11054
import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))

dp = [[0, 0] for _ in range(n)]
for i in range(n):
    long, short = 1, 1
    for j in range(i):
        if arr[j] < arr[i]:
            long = max(long, dp[j][0]+1)
        elif arr[j] > arr[i]:
            short = max(short, max(dp[j])+1)

    dp[i][0] = long
    dp[i][1] = short

res = 0
for i in range(n):
    tmp = max(dp[i])
    res = max(tmp, res)

print(res)