import sys
input = sys.stdin.readline

p = [0, 1, 1, 1, 2, 2]

for _ in range(6, 101):
    p.append(p[-1]+p[-5])

# print(p)

t = int(input())
for _ in range(t):
    print(p[int(input())])