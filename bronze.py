import sys
from collections import deque
input = sys.stdin.readline



    


n = int(input())
a, b = map(int, input().split())
m = int(input())
data = [list(map(int, input().split())) for _ in range(m)]
visited = [False] * (n+1)

table = [[] for _ in range(n+1)]
for d in data:
    x = d[0]
    y = d[1]
    table[x].append(y)
    table[y].append(x)

# print(table)

queue = deque([a])  # 큐를 초기화하고 시작 노드를 추가

count = 0
while queue:
    node = queue.popleft()  # 큐의 맨 앞에서 노드를 꺼냄
    # print(node)  # 방문한 노드 출력 (원하는 작업 수행)
    count += 1
    visited[node] = True # 방문 처리
    for n in table[node]:
        if n == b:
            print(count)
            exit()
        if not visited[n]:
            queue.append(n)  # 미방문 이웃 노드를 큐에 추가

print(-1)