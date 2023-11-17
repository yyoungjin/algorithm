# 16724
import sys
sys.setrecursionlimit(10**7)


def find(x, y):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x][y] != (x, y):
        parent[x][y] = find(parent[x][y][0], parent[x][y][1])
    return parent[x][y]


def union(x1, y1, x2, y2):
    a1, a2 = find(x1, y1)
    b1, b2 = find(x2, y2)
    if a1 < b1 or (a1 == b1 and a2 < b2):
        parent[b1][b2] = (a1, a2)
    else:
        parent[a1][a2] = (b1, b2)


def dfs(x, y):
    visited[x][y] = 1
    dir = ['U', 'D', 'L', 'R']
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    idx = dir.index(table[x][y])
    nx, ny = x+dx[idx], y+dy[idx]
    if 0<=nx<n and 0<=ny<m and parent[nx][ny] != parent[x][y]:
        union(x, y, nx, ny)
        dfs(nx, ny)


n, m = map(int, input().split())
table = [list(sys.stdin.readline().rstrip()) for _ in range(n)]

# parent 를 자기자신으로 설정
parent = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        parent[i][j] = (i, j)

visited = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            dfs(i, j)



res = set()
# print(parent)
for i in range(n):
    for j in range(m):
        find(i, j)
        if table[i][j] not in res:
            res.add(parent[i][j])

print(len(res))