# 27172
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
max_num = max(arr)

dp = {}
for i in range(n):
    dp[arr[i]] = 0

for num in arr:
    for i in range(num*2, max_num+1, num):
        if i in dp:
            dp[i] -= 1
            dp[num] += 1

res = list(dp.values())
print(' '.join(map(str, res)))