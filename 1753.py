import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수, 간선의 개수를 입력받기
V, E = map(int, input().split())
start = int(input())
graph = [[] for i in range(V+1)]
distance = [INF] * (V+1)

for i in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))



def short_distance(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

short_distance(start)
for d in range(1, len(distance)):
    if distance[d] == INF:
        print("INF")
    else: 
        print(distance[d])