# 위상 정렬
import sys
input = sys.stdin.readline
from collections import deque
t = int(input())

def test():
    n = int(input())
    table = [[] for _ in range(n+1)]
    arr = [0] * (n+1)
    change = set()
    past_rank = [0] + list(map(int, input().split()))
    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())
        change.add((a, b))
    
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            a = past_rank[i]
            b = past_rank[j]
            if (b, a) in change or (a, b) in change:
                a, b = b, a
            table[a].append(b)
            arr[b] += 1

    q = deque([])
    res = []
    # 시작점 찾기
    for i in range(1, n+1):
        if not arr[i]:
            q.append(i)
            arr[i] -= 1 # 방문처리

    while q:
        node = q.popleft()
        res.append(str(node)) # 결과에 기록
        # 노드 제거
        for i in table[node]:
            arr[i] -= 1
            if arr[i] == 0:
                q.append(i)
                arr[i] -= 1

    if len(res) != n:
        return "IMPOSSIBLE"
    return ' '.join(res)


rst = []
for _ in range(t):
    rst.append(test())

for i in rst:
    print(i)