# 냅색 알고리즘

import sys
input = sys.stdin.readline

n, k = map(int, input().split())

table = [0] * (k+1)
for _ in range(n):
    w, v = map(int, input().split())
    if w > k:
        continue
    for j in range(k, 0, -1):
        if j + w <= k and table[j] != 0:
            table[j+w] = max(table[j+w], table[j] + v)
    table[w] = max(table[w], v)
print(max(table))