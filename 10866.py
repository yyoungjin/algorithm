import heapq
import sys
input = sys.stdin.readline

n = int(input())
data = []
ans = []
count = 0

for _ in range(n):
    num = int(input())
    if num == 0:
        if len(data) == 0:
            ans.append(0)
        else:
            ans.append(heapq.heappop(data))
    else:
        heapq.heappush(data, num)

for a in ans:
    print(a)
