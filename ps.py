import sys
from collections import deque

def bfs(start, end):
    if start == end:
        return (0, 1)
    q = deque([start])
    arr = [-1] * (100001)
    arr[start] = 0
    rst = 0
    count = 0
    while q:
        x = q.popleft()
    
        for i in range(3):
            if i == 0:
                nx = x-1
            elif i == 1:
                nx = x+1
            else:
                nx = x*2
            if 0<= nx <= 100000:
                if (nx == end):
                    if rst == 0:
                        rst = arr[x] + 1
                        count += 1
                    elif arr[x]+1 == rst:
                        count += 1
                if (arr[nx] == -1 or arr[nx] == arr[x] + 1) and count == 0:
                    q.append(nx)
                    arr[nx] = arr[x]+1

    return (rst, count)

input = sys.stdin.readline
start, end = map(int, input().split())
num = bfs(start, end)
for r in num:
    print(r)