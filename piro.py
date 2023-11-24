import sys
input = sys.stdin.readline
from itertools import combinations
import bisect

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

comb = combinations([i for i in range(n)], 2)
cnt = 1e10
for a, b in comb:
    l = arr[a]+arr[b]
    tmp2 = bisect.bisect_left(arr, -l)
    tmp1 = tmp2 - 1

    while tmp1 == a or tmp1 == b:
        tmp1 -= 1
    while tmp2 == a or tmp2 == b:
        tmp2 += 1
    
    if 0<= tmp1 < n and 0<= tmp2<n:
        if abs(l+arr[tmp1]) < abs(l+arr[tmp2]):
            tmp = tmp1
        else:
            tmp = tmp2
    elif 0<= tmp1 < n:
        tmp = tmp1
    else:
        tmp = tmp2

    if abs(l+arr[tmp]) < cnt:
        cnt = abs(l+arr[tmp])
        res = (arr[a], arr[b], arr[tmp])

print(' '.join(map(str, res)))
