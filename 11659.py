import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
data = [0] * (n+1)
num = 0
for d in range(1, n+1):
    num += arr[d-1]
    data[d] = num

for _ in range(m):
    i, j = map(int, input().split())
    print(data[j] - data[i-1])