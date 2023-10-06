import sys
import math
import heapq
 
def dijkstra(graph, n, source, sink1, sink2):
  dist = [math.inf] * n
  pq = []
  dist[source] = 0
  heapq.heappush(pq, (0, source))
  while len(pq) != 0:
    cost, node = heapq.heappop(pq)
    for i in range(1, n):
      nextCost = dist[node] + graph[node][i]
      if nextCost < dist[i]:
        dist[i] = nextCost
        heapq.heappush(pq, (nextCost, i))
  return dist[sink1], dist[sink2]
 
def solve():
  n, e = map(int, sys.stdin.readline().rstrip().split())
  graph = [[math.inf] * (n+1) for _ in range(n+1)]
  for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    graph[a][b] = c
    graph[b][a] = c
  v1, v2 = map(int, sys.stdin.readline().rstrip().split())
  a, d = dijkstra(graph, n+1, 1, v1, v2)
  b, f = dijkstra(graph, n+1, v1, v2, n)
  c, e = dijkstra(graph, n+1, v2, n, v1)
  rst = min(a+b+c, d+e+f)
  if rst != math.inf:
    print(rst)
  else:
    print(-1)
 
solve()