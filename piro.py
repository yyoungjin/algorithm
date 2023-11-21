#### 에드몬드카프 알고리즘
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
from collections import deque

N, p = map(int, input().split())
n = N*2

# graph, capacity, flow
graph = [[] for _ in range(n+1)]
capacity = [[0] * (n+1) for _ in range(n+1)]
flow = [[0] * (n+1) for _ in range(n+1)]

# graph update _u -> v
for _ in range(p):
    u, v = map(int, input().split())
    _u = u + N
    _v = v + N
    graph[_u].append(v)
    graph[v].append(_u) # 음수 유량 고려
    capacity[_u][v] = 1

    graph[_v].append(u)
    graph[u].append(_v)
    capacity[_v][u] = 1

# u -> _u
for u in range(1, N+1):
    _u = u + N
    graph[u].append(_u)
    graph[_u].append(u)
    capacity[u][_u] = 1

def bfs_path(source, sink, visited): # source부터 sink까지 흘릴 수 있는 추가 유량이 있는지, 있다면 그 경로를 visited에 저장
    q = deque()
    q.append(source)
    while q and visited[sink] == -1: # 갈 곳이 남아있고, 아직 도착점에 도달 안했다면 반복
        u = q.popleft()
        for v in graph[u]: # 역방향을 포함하여 연결된 다음 정점 모두 순회
            leftover_flow = capacity[u][v] - flow[u][v]
            if visited[v] == -1 and leftover_flow > 0: # 방문한 적 없고, 잔여용량 남아 있으면 방문
                q.append(v)
                visited[v] = u # 어디서 왔는지 기록
                if v == sink: # sink에 도착했다면 종료
                    break

    if visited[sink] == -1: # 경로가 없다는 뜻
        return False
    
    return True

def edmonds_karp(source, sink):
    ans = 0
    while True: # 업데이트할 유량이 있으면 반복, 즉 bfs 결과에 따라 결정
        visited = [-1] * (n+1)
        if not bfs_path(source, sink, visited): # path 가 없다면 업데이트 종료
            break
        
        # 위에서 찾은 min_flow를 flow에 업데이트
        j = sink
        while j != source:
            i = visited[j]
            flow[i][j] += 1
            flow[j][i] -= 1
            j = i

        ans += 1

    return ans

print(edmonds_karp(1+N, 2))