# 6236
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))
    


start, end = max(arr), sum(arr)
while start <= end:
    mid = (start + end) // 2
    count, left = 1, mid
    for i in arr:
        if i > left:
            count += 1
            left = mid
        left -= i

    if count <= m:
        res = mid
        end = mid - 1
    else: 
        start = mid + 1
        
print(res)

