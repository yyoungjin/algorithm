# 16946
import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
table = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]

visited = [[0] * m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, num):
    visited[x][y] = num
    q = deque([(x, y)])

    res = set()
    while q:
        x, y = q.popleft()
        res.add((x, y))
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and table[nx][ny] == 0:
                visited[nx][ny] = num
                q.append((nx, ny))

    return len(res)

rst = {}
walls = []
num = 2
for i in range(n):
    for j in range(m):
        if not visited[i][j] and table[i][j] == 0:
            rst[num] = bfs(i, j, num)
            num += 1
        elif table[i][j] == 1:
            walls.append((i, j))

for i, j in walls:
    count = 0
    tmp = set()
    for d in range(4):
        ni = dx[d] + i
        nj = dy[d] + j
        if 0<=ni<n and 0<=nj<m and visited[ni][nj] > 1:
            num = visited[ni][nj]
            if num not in tmp:
                count += rst[num]
                tmp.add(num)

    table[i][j] = (count + 1) % 10

for line in table:
    print(''.join(map(str, line)))
