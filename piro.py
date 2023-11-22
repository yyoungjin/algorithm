# 16469
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
table = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
visited_A = [[-1] * M for _ in range(N)]
visited_B = [[-1] * M for _ in range(N)]
visited_C = [[-1] * M for _ in range(N)]

A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))



def bfs(visited, start):
    x, y = start
    visited[x][y] = 0
    q = deque([(x, y)])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M and (visited[nx][ny] == -1) and table[nx][ny] == 0:
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
    return visited

bfs(visited_A, (A[0]-1, A[1]-1))
bfs(visited_B, (B[0]-1, B[1]-1))
bfs(visited_C, (C[0]-1, C[1]-1))

min_time = 1e9
res = []
for i in range(N):
    for j in range(M):
        a = visited_A[i][j]
        b = visited_B[i][j]
        c = visited_C[i][j]
        if a == -1 or b == -1 or c == -1:
            continue
        
        if min_time > max(a, b, c):
            res = [[i, j]]
            min_time = max(a, b, c)

        elif min_time == max(a, b, c):
            res.append([i, j])
        
if len(res):
    print(min_time)
    print(len(res))
else:
    print(-1)