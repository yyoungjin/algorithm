import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

# matched_Y : Y 그룹의 노드와 매칭된 X 노드의 번호
# matched_X : X 그룹의 노드와 매칭된 Y 노드의 번호
def dfs(x):
    visited[x] = True
    for y in graph[x]:
        # y 노드와 매칭된 노드가 없는 경우, x 노드와 매칭
        if matched_Y[y] == 0:
            matched_Y[y] = x
            matched_X[x] = y
            return True
        # y 노드가 이미 매칭이 되어있는 경우, y 노드와 매칭되어 있는 노드가 다른 노드와 매칭이 가능한지 확인
        elif not visited[matched_Y[y]] and dfs(matched_Y[y]):
            # 다른 노드와 매칭이 가능한 경우, y 노드와 x 노드를 매칭
            matched_Y[y] = x
            matched_X[x] = y
            return True
    return False

A, B = map(int, input().split())
graph = [[] for _ in range(A+1)]
matched_X = [0] * (A+1)
matched_Y = [0] * (B+1)

m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

cnt = 0
for i in range(1, A+1):
    if matched_X[i] == 0:
        visited = [False] * (A+1)
        if dfs(i):
            cnt += 1

print(cnt)

# 거의 이분그래프 추가 매칭

