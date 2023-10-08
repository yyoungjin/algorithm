# 13549

import sys
from collections import deque

def bfs(start, end):
    if start == end:
        return 0
    q = deque([start])
    arr = [-1] * (100001)
    arr[start] = 0
    while q:
        x = q.popleft()
    
        for i in range(3):
            if i == 0:
                nx = x-1
                tmp = 1
            elif i == 1:
                nx = x+1
                tmp = 1
            else:
                nx = x*2
                tmp = 0
            if 0<= nx <= 100000:
                if arr[nx] == -1 or arr[x]+tmp < arr[nx]:
                    arr[nx] = arr[x]+tmp
                    q.append(nx)
    return arr[end]

input = sys.stdin.readline
start, end = map(int, input().split())
num = bfs(start, end)
print(num)