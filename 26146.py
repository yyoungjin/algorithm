## kosaraju 알고리즘 (SCC알고리즘)
# input
V, E = map(int, input().split())
visited = [0] * (V+1)
graph = [[] for _ in range(V+1)]

# 주어진 간선에 따라 그래프 생성
for _ in range(E):
    start, end = map(int, input().split())
    graph[start].append(end)

# v 노트에 대해서,,
def dfs(v, visited, stack):
    #방문처리
    visited[v] = 1

    for w in graph[v]:
        if visited[w] == 0:
            stack.append(w)
            dfs(w, visited, stack)
    stack.append(v)


def reverseGraph():
    reverse_graph = [[] for i in range(V+1)]
    for i in range(1, V+1):
        for j in graph[i]:
            reverse_graph[j].append(i)
    return reverse_graph


def reverseDfs(v, visited, stack):
    visited[v] = 1
    stack.append(v)
    for w in reverse_graph[v]:
        if visited[w] == 0:
            reverseDfs(w, visited, stack)

    
stack = []
for i in range(1, V+1):
    if visited[i] == 0:
        dfs(i, visited, stack)

reverse_graph = reverseGraph()

visited = [0] * (V+1)
results = []

while stack:
    ssc = []
    node = stack.pop()
    if visited[node] == 0:
        reverseDfs(node, visited, ssc)
        results.append(sorted(ssc))

# print(results)
if len(results) == 1:
    print("Yes")
else:
    print("No")

# failed