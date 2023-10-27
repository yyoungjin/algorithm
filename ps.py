# 2206
import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
table = []
dp = [[False] * m for _ in range(n)]
dp_crack = [[False] * m for _ in range(n)]

for _ in range(n):
    table.append(list(map(int, sys.stdin.readline().rstrip())))

# 0은 파괴 가능 1은 불가능
q = deque([(0, 0, 0)])
dp[0][0] = 1
while q:
    x, y, c = q.popleft()
    if x == n-1 and y == m-1:
        break

    if table[x][y]:
        c = 1
        dp_crack[x][y] = dp[x][y]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0<=nx<n and 0<=ny<m:
            if not c: # 파괴 가능하다면
                if not dp[nx][ny]:
                    dp[nx][ny] = dp[x][y]+1
                    q.append((nx, ny, c))

            elif not dp_crack[nx][ny] and dp_crack[x][y] and c: # 파괴 불가능에 다음이 지나갈 수 있는 길이라면
                dp_crack[nx][ny] = dp_crack[x][y] + 1
                q.append((nx, ny, c))

        

if dp[n-1][m-1] and dp_crack[n-1][m-1]:
    print(min(dp[n-1][m-1], dp_crack[n-1][m-1]))
elif dp[n-1][m-1]:
    print(dp[n-1][m-1])
elif dp_crack[n-1][m-1]:
    print(dp_crack[n-1][m-1])
else:
    print(-1)