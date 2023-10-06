import sys
input = sys.stdin.readline

n, m = map(int, input().split())
table = []
for _ in range(n):
    table.append(list(map(int, input().split())))

arr = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        a,b,c = 0,0,0
        if i - 1 >= 0:
            a = table[i-1][j]
        if j - 1 >= 0:
            b = table[i][j-1]
        if i - 1 >= 0 and j-1 >= 0:
            c = table[i-1][j-1]
        arr[i][j] = max(a,b,c) + table[i][j]
        table[i][j] = arr[i][j]

print(arr[i][j])