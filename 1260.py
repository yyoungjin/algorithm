import sys
input = sys.stdin.readline
from collections import deque


N, M, V = map(int, input().split())
graph = [[] for i in range(N+1)]
visited1 = [False] * (N+1)
visited2 = [False] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# print(graph)

for j in range(N+1):
    graph[j] = sorted(graph[j])

# print(graph)

dfslist = []
def dfs(V):
    dfslist.append(str(V))
    visited1[V] = True
    for v in graph[V]:
        if not visited1[v]:
            dfs(v)
    

bfslist = []
def bfs(V):
    q = deque([V])
    visited2[V] = True
    while q:
        v = q.popleft()
        bfslist.append(str(v))
        for i in graph[v]:
            if not visited2[i]:
                q.append(i)
                visited2[i] = True





dfs(V)
bfs(V)
print(' '.join(dfslist))
print(' '.join(bfslist))
