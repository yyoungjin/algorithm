# 유니온파인드 알고리즘

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100_000)

n, m = map(int, input().split())
p = [i for i in range(n+1)]


def find(a):
    if a == p[a]:
        return a
    p[a] = find(p[a])
    return p[a]


def union(a, b):
    pa = find(a)
    pb = find(b)
    if pa < pb:
        p[pb] = pa
    else:
        p[pa] = pb

table = [0] * (n+1)

for _ in range(m):
    q, a, b = map(int, input().split())
    if q == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')