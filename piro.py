# 15652
import sys
from itertools import combinations_with_replacement
input = sys.stdin.readline

n, m = map(int, input().split())

arr = [x for x in range(1, n+1)]
comb = combinations_with_replacement(arr, m)

for c in comb:
    print(' '.join(list(map(str, c))))