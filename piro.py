# 12015
import sys
import bisect
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))

dp = [arr[0]]
table = []
for i in range(n):
    if arr[i] > dp[-1]:
        dp.append(arr[i])
        table.append((arr[i], len(dp)-1))

    else:
        idx = bisect.bisect_left(dp, arr[i])
        dp[idx] = arr[i]
        table.append((arr[i], idx))

count = len(dp)
print(count)

res = [0] * count
for num, idx in table[::-1]:
    if idx == count - 1:
        res[idx] = num
        count -= 1

print(' '.join(map(str, res)))
