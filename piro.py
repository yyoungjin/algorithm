# 15663
import sys
from itertools import permutations
input = sys.stdin.readline

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
comb = permutations(arr, m)

for c in sorted(list(set(comb))):
    print(' '.join(list(map(str, c))))