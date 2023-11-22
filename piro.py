#10942
import sys
input = sys.stdin.readline

n = int(input())
arr = [0] + list(map(int, input().split()))
dp = [[0] * (n+1) for _ in range(n+1)]


for i in range(0, n): # 간격 설정
    for start in range(1, n+1-i):
        end = start + i 
        if start == end : # 1글자
            dp[start][end] = 1 
        elif arr[start] == arr[end] : 
            if start + 1 == end: # 2글자
                dp[start][end] = 1 
            elif dp[start+1][end-1] == 1: #3글자 이상
                dp[start][end] = 1 


m = int(input())
for _ in range(m):
    s, e = map(int, input().split())
    print(dp[s][e])