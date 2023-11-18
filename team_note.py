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