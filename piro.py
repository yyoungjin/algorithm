#22871
import sys
input = sys.stdin.readline
INF = 999999999

n = int(input())
arr = list(map(int, input().split()))

dp = [0] * n # 매 위치마다 k의 최소값을 저장하자

# j 위치일 때, 이전 위치들을 전부 돌며 k최소값을 구한다?
for j in range(1, n):
    k = INF
    #O(n)
    for i in range(j):
        tmp = (j - i) * (abs(arr[i] - arr[j]) + 1)
        tmp = max(tmp, dp[i])
        k = min(k, tmp)

    #O(log(n))



    dp[j] = k

print(dp[-1])