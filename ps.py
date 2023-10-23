# 위상 정렬
from collections import deque
n, m = map(int, input().split())
table = [[] for _ in range(n+1)]
visited = [False] * (n+1)
arr = [0] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())
    table[a].append(b) # 다음 갈 곳
    arr[b] += 1 # 내가 실행되는 조건의 수

q = deque([])
res = []
# 시작점 찾기
for i in range(1, n+1):
    if not arr[i]:
        q.append(i)
        visited[i] = True

while q:
    node = q.popleft()
    res.append(str(node)) # 결과에 기록
    # 노드 제거
    for i in table[node]:
        arr[i] -= 1
        if arr[i] == 0:
            if not visited[i]:
                q.append(i)
                visited[i] = True

print(' '.join(res))