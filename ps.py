# 1043
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
t_people = set(list(map(int, input().split()))[1:])

people = [[] for _ in range(n+1)]
parties = []
rst = []
for _ in range(m):
    party = set(list(map(int, input().split()))[1:])
    parties.append(party)
    rst.append(party)

while True:
    flag = False
    for i in range(len(parties)):
        if len(t_people & parties[i]) > 0:
            t_people = t_people | parties[i]
            parties[i] = set()
            flag = True

    if not flag:
        break

res = 0
for party in rst:
    if len(t_people & party) == 0:
        res += 1
print(res)

