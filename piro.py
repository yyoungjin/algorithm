#20040
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

import sys
input = sys.stdin.readline

# 노드의 개수와 간선(Union 연산)의 개수 입력 받기
n, m = map(int, input().split())
parent = [0] * n

for i in range(n):
    parent[i] = i

# Union 연산을 각각 수행
flag = 0
for i in range(m):
    a, b = map(int, input().split())
    if flag:
        continue
    if find(a) == find(b):
        flag = i+1
    union(a, b)

if flag:
    print(flag)
else:
    print(0)
