N, M = map(int, input().split())
graph = []
visited = [[False]*M for _ in range(N)]

start = False
for i in range(N):
    m = list(input())
    for mi in range(M):
        if m[mi] == ".":
            m[mi] = '@'
    graph.append(m)
    if (i == 0 or i == N-1) and ("@" in m):
        j = m.index("@")
        if not start:
            start = (i, j)
        else:
            end = (i, j)
    if m[0] == "@":
        if not start:
            start = (i, 0)
        else:
            end = (i, 0)
    if m[-1] == "@":
        if not start:
            start = (i, M-1)
        else:
            end = (i, M-1)
        

# 시작점 찾았다

path = []
res = []
def dfs(start, path):
    path.append(start)
    # end에 도착했을 경우
    if start == end:
        if len(res) == 0:
            for p in path:
                res.append(p)
    x = start[0]
    y = start[1]
    visited[x][y] = True

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for r in range(4):
        if is_valid(x+dx[r], y+dy[r]):
            if not visited[x+dx[r]][y+dy[r]] and graph[x+dx[r]][y+dy[r]] == "@":
                dfs((x+dx[r], y+dy[r]), path)

    #아 이 길이 아니구나.. 스택 삭제!
    path.pop()


def is_valid(x, y):
    if 0 <= x < N and 0 <= y < M:
        return True
    else:
        return False
    
dfs(start, path)
for cg in res:
    graph[cg[0]][cg[1]] = "."

for gp in graph:
    gp = ''.join(gp)
    print(gp)

# 실패