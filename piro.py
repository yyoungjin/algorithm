# 15657
import sys
from itertools import combinations_with_replacement
input = sys.stdin.readline

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
comb = combinations_with_replacement(arr, m)

for c in sorted(comb):
    print(' '.join(list(map(str, c))))