import sys
input = sys.stdin.readline

k = int(input())
data = []
for _ in range(k):
    a = int(input())
    if a == 0:
        data.pop()
    else:
        data.append(a)

print(sum(data))