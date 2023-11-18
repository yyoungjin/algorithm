import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

A, B = map(int, input().split())
graph = [[] for _ in range(A + 1)]

m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

if (A * B) % 2 == 0:
    print((A//2 + B//2))
    exit()

else:
    flag = 0
    for a in range(1, A+1, 2):
        for b in graph[a]:
            if b%2 == 1:
                flag = 1
                break

if flag:
    print((A+B) // 2)
else:
    print((A+B)//2 - 1)