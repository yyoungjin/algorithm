#16236
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
table = []
visited = [[-1] * n for _ in range(n)]
shark = 2

for _ in range(n):
    table.append(list(map(int, input().split())))

# O(n^2)로 아기상어 위치를 찾는다.
def find_shark():
    for i in range(n):
        for j in range(n):
            if table[i][j] == 9:
                table[i][j] = 0
                return (i, j)
            
# BFS - 먹이 좌표 탐색
def bfs(x, y, shark):
    q = deque([(x, y)])
    visited[x][y] = 0
    
    # 상좌우하 순서로 탐색
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]
    fishes = []
    while q:
        x, y = q.popleft()

        # 먹을지 지나갈지 결정, 상어 시작 위치라면 패스
        if table[x][y] != 0 and table[x][y] < shark:
            fishes.append([visited[x][y], x, y])
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and (visited[nx][ny] == -1) and table[nx][ny] <= shark:
                # nx 방문처리
                visited[nx][ny] = visited[x][y] + 1
                if fishes and visited[nx][ny] > fishes[0][0]:
                    continue
                q.append((nx, ny))
        
    if fishes:
        fishes.sort()
        x, y = fishes[0][1], fishes[0][2]
        table[x][y] = 0 # 냠!! 여기 기준으로 다시 탐색!!
        return fishes[0]

    return 0


# 상어 위치
x, y = find_shark()

# 더이상 먹을 것이 없을 때까지 반복
time = 0
ate = 0
while True:
    # 먹이의 좌표, 걸린 시간
    fish = bfs(x, y, shark)

    if fish: # 남은 먹이가 있다면,
        count_time, x, y = fish[0], fish[1], fish[2]
        time += count_time
        visited = [[-1] * n for _ in range(n)]
        ate += 1
        if shark == ate:
            shark += 1
            ate = 0

    else:
        print(time)
        break