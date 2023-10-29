# 2638
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

n, m = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 바깥에서 공기를 확산시키고 닿는 면적이 2면 이상인 c를 확보

# 1. 가장자리에서 공기 확산시키기 
def dfs(x, y):
    # 확산처리
    table[x][y] = -1

    # 상하좌우로 확산
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0<=nx<n and 0<=ny<m and table[nx][ny] == 0:
            dfs(nx, ny)

# 초기 확산
for j in [0, m-1]:
    for i in range(n):
        dfs(i, j)
for i in [0, n-1]:
    for j in range(1, m-1):
        dfs(i, j)

# 2. c 표시
def c_check():
    clist = []
    for i in range(1, n-1):
        for j in range(1, m-1):
            if table[i][j] == 1:
                count = 0
                for t in range(4):
                    nx = dx[t] + i
                    ny = dy[t] + j
                    if table[nx][ny] == -1:
                        count += 1
                if count >= 2:
                    clist.append([i, j])
                    table[i][j] = 'c'
    return clist

count = 0
while True:
    clist = c_check()
    if not clist:
        break
    for i, j in clist:
        dfs(i, j)
    count += 1



# for i in range(n):
#     print(table[i])

print(count)