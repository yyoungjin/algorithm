# 위상 정렬
import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
table = [[] for _ in range(n+1)]
arr = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    table[a].append(b)
    arr[b] += 1

q = []
res = []
# 시작점 찾기
for i in range(1, n+1):
    if not arr[i]:
        heapq.heappush(q, i)
        arr[i] -= 1 # 방문처리

while q:
    node = heapq.heappop(q)
    res.append(str(node)) # 결과에 기록
    # 노드 제거
    for i in table[node]:
        arr[i] -= 1
        if not arr[i]:
            heapq.heappush(q, i)

print(' '.join(res))