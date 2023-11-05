import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

# 유니온 파인드

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b


n, m, k = map(int, input().split())
k -= 1
values = [0] + list(map(int, input().split()))

parent = [x for x in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    union(a, b)

groups = [0] * (n+1)
for i in range(1, n+1):
    if i != parent[i]:
        I = find(i) # 최적화
        values[I] += values[i]
        groups[I] += 1
    else:
        groups[i] += 1


# 냅색 알고리즘
table = [0] * (k+1)

for i in range(1, n+1):
    if groups[i] != 0:
        w = groups[i]
        v = values[i]
        if w > k:
            continue
        for j in range(k, 0, -1):
            if j + w <= k and table[j] != 0:
                table[j+w] = max(table[j+w], table[j] + v)
        table[w] = max(table[w], v)

print(max(table))
