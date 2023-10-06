import sys

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())
arr = []
for i in range(N):
   temp = list(map(int, sys.stdin.readline().split()))
   arr.append(temp)
ans = 1
arr[r][c] = -1
while arr[r][c] != 1:
   flag = 0
   for i in range(4):
       d = (d - 1) % 4
       temp = r + dx[d]
       tempp = c + dy[d]
       if arr[temp][tempp] == 0:
           r, c = temp, tempp
           arr[r][c] = -1
           ans += 1
           flag = 1
           break
   if not flag:
       r += dx[d - 2]
       c += dy[d - 2]

print(ans)