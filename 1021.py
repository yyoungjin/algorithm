import sys
input = sys.stdin.readline

data = []
n, c = map(int, input().split())
for _ in range(n):
    d, t, p = map(int, input().split())
    x = d-t+1
    data.append([x, p])

data.sort(key = lambda x: (x[0], -x[1]))

print(data)
count = 1
for i in data:
    if i[0] 