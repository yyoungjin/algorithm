N, M = map(int, input().split())
data = [[], [], [], [], [], [], [], [], []]

for _ in range(M):
    u, v, w = map(int, input().split())
    data[u].append((v, w))

print(data)
city_value = [0] * N

def dfs(start, count, value):
    if count == 9:
        city_value[start] = city_value[start] + value
        print(city_value[start])
        return
    # start 도시에서 출발해서 가는 곳들을 for문으로 전부 가기
    for n in data[start]:
        value *= (n[1]/100)
        dfs(n[0], count+1, value)

dfs(0, 0, 1)
print(city_value)
sum = 0
for dd in city_value:
    sum += dd

print(sum)


# 실패