import heapq

n, m = map(int, input().split())

people = {}
table = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    table[b].append(a) # 노트북을 기준으로
    people[a] =  # 사람을 기준으로
    
heapq.heapify(people)

print(people)
res = 0
while people:
    p = heapq.heappop(people)
    if p[0] > 0:
        for _ in table[p[1]]