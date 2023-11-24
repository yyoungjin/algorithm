# 위상정렬
from collections import deque
import sys
input = sys.stdin.readline
v, m = map(int, input().split()) # v는 노드 수 e는 간선 수, m은 pd수
indegree = [0] * (v+1)
graph = [[] for i in range(v + 1)]

for _ in range(m):
    tmp = list(map(int, input().split()))
    for i in range(1, tmp[0]):
        a, b = tmp[i], tmp[i+1]
        graph[a].append(b)
        indegree[b] += 1

def topology_sort():
    result = []
    q = deque()
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)
        
    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    
    return result

res = topology_sort()
if len(res) < v:
    print(0)
else:
    for r in res:
        print(r)