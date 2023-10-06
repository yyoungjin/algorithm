import sys

n = int(input())
table = {}
for i in range(65, 91):
    table[chr(i)] = [chr(i)]

print(table)
for _ in range(n):
    a, b, f = map(str, sys.stdin.readline().strip().split())
    f = int(f)
    tmp = table[a]
    table[a] = tmp.append((b, f))
    print(table[a])

print(table)
