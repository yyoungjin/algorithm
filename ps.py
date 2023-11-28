# 17244
import sys
from collections import deque
from itertools import permutations
n, m = map(int, sys.stdin.readline().split())
table = [list(sys.stdin.readline().rstrip()) for _ in range(m)]

X = [0]
count = 1
for i in range(m):
    for j in range(n):
        if table[i][j] == 'X':
            X.append((i, j))
            table[i][j] = count
            count += 1
        elif table[i][j] == 'S':
            table[i][j] = 0
            S = (i, j)
        elif table[i][j] == 'E':
            table[i][j] = 6
            E = (i, j)
X[0] = S
X.append(E)

INF = 1e9
graph = [[INF] * 7 for _ in range(7)]

def bfs(node):
    x, y = X[node]
    visited[x][y] = 0
    q = deque([(x, y)])
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0<=nx<m and 0<=ny<n and table[nx][ny] != '#' and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1

                if table[nx][ny] != '.':
                    graph[node][table[nx][ny]] = visited[nx][ny]
                    graph[table[nx][ny]][node] = visited[nx][ny]

                q.append((nx, ny))

if len(X) == 2:
    visited = [[-1] * n for _ in range(m)]
    bfs(0)
    print(graph[0][6])
    exit()

for node in range(1, len(X)-1):
    visited = [[-1] * n for _ in range(m)]
    bfs(node)

comb = permutations([i for i in range(1, len(X))], len(X)-2)

res = INF
for c in comb: 
    c = list(c)
    num = 0
    sp = 0
    while c:
        ep = c.pop()
        num += graph[sp][ep]
        sp = ep

    num += graph[sp][6]
    res = min(num, res)
    
                
print(res)