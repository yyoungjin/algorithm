#### 유니온파인드
def find(x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(Union 연산)의 개수 입력 받기
v, e = map(int, input().split())
parent = [0] * (v + 1) 
for i in range(1, v + 1):
    parent[i] = i

# Union 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union(a, b)

#### 이분매칭 알고리즘
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


#### 소수판별
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


#### 에드몬드카프 알고리즘
# graph, capacity, flow
graph = [[] for _ in range(n+1)]
capacity = [[0] * (n+1) for _ in range(n+1)]
flow = [[0] * (n+1) for _ in range(n+1)]

# graph update u -> v
for _ in range(p):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u) # 음수 유량 고려
    capacity[u][v] = 

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
        
        ## min_flow 찾는 과정
        min_flow = 1e9
        j = sink
        while j != source:
            i = visited[j]
            leftover_flow = capacity[i][j] - flow[i][j]
            min_flow = min(min_flow, leftover_flow)
            j = i
        
        # 위에서 찾은 min_flow를 flow에 업데이트
        j = sink
        while j != source:
            i = visited[j]
            flow[i][j] += min_flow
            flow[j][i] -= min_flow
            j = i

        ans += min_flow

    return ans