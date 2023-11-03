# 11053
import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))

dp = [0] * n
table = [[] for _ in range(n)]

for i in range(n):
    count = 1
    tmp = [arr[i]]
    for j in range(i):
        if arr[j] < arr[i]:
            if count < (dp[j]+1):
                count = dp[j]+1
                tmp = table[j] + [arr[i]]


    dp[i] = count
    table[i] = tmp

max_value = max(dp)
max_table = table[dp.index(max_value)]

print(max_value)
print(' '.join(map(str, max_table)))