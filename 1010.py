# 다이나믹 프로그래밍

import sys
input = sys.stdin.readline

table = [0,0,0] # rgb
n = int(input())
for _ in range(n):
    r, g, b = table[0], table[1], table[2]
    nr, ng, nb = map(int, input().split())

    table[0] = nr + min(g, b)
    table[1] = ng + min(b, r)
    table[2] = nb + min(r, g)
print(min(table))

