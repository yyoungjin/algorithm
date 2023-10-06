import sys
sys.setrecursionlimit(10**6)

def dfs(start, graph, visited):
    visited[start] = True
    for j in graph[start]:
        if not visited[j]:
            dfs(j, graph, visited)


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

count = 0
for node in range(1, n+1):
    if not visited[node]:
        count += 1
        dfs(node, graph, visited)

print(count)
    

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# dfs 함수
def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

n, m = map(int, input().split()) # 정점의 개수, 간선의 개수
graph = [[] for _ in range(n+1)]
for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

count = 0 # 연결 노드의 수
visited = [False] * (n+1)
for i in range(1, n+1):
    if not visited[i]:
        dfs(graph, i, visited)
        count += 1 # dfs 한 번