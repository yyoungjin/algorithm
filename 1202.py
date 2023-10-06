import heapq
import sys

N, K = map(int, sys.stdin.readline().split())
jew = []
for _ in range(N):
    heapq.heappush(jew, list(map(int, sys.stdin.readline().split())))
bags = []
for _ in range(K):
    bags.append(int(sys.stdin.readline()))
bags.sort()

answer = 0
tmp_jew = []
for bag in bags:
    # 우선 당연히 가방에 넣을 수 있는 무게가 가장 가벼운 보석은 넣을 수 있는 크기여야 하니까
    while jew and bag >= jew[0][0]:
        # 이 가방에 넣을 수 있는 보석들을 따로 빼놓는거임 (가방이 점점 커지면 그만큼 더 가능해진 보석을을 추가하는 ㅎ)
        heapq.heappush(tmp_jew, -heapq.heappop(jew)[1])
    # 이 가방에 넣을 수 있는 보석 중에서 가장 비싼 걸 넣음
    if tmp_jew:
        answer -= heapq.heappop(tmp_jew)
    # 더이상 넣을 보석이 없으면 중단
    elif not jew:
        break
print(answer)