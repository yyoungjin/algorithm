# 13913

import sys
from collections import deque

def bfs(start, end):
    q = deque([start])
    arr = [0] * 100001
    path = [0] * 100001
    while q:
        x = q.popleft()
        if x == end:
            print(arr[x])
            res = str(x)
            a = x
            for _ in range(arr[x]):
                a = path[a]
                res = str(a) + ' ' + res
            print(res)
            return
        for nx in (x-1, x+1, 2*x):
            if 0<= nx <= 100000 and arr[nx] == 0:
                q.append(nx)
                arr[nx] = arr[x] + 1
                path[nx] = x # x로부터 왔다는 것을 기록

input = sys.stdin.readline
start, end = map(int, input().split())
bfs(start, end)