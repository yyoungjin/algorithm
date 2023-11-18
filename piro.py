import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    table = []
    for _ in range(m):
        a, b = map(int, input().split())
        table.append([a, b])

    table.sort(key = lambda x : (x[1], -x[0]))

    taken = [0] * (n + 1)
    cnt = 0
    for p in table:
        for book in range(p[0], p[1]+1):
            if not taken[book]:
                taken[book] = 1
                cnt += 1
                break
    print(cnt)