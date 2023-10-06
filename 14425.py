N, M = map(int, input().split())
S = set()
test = set()

for _ in range(N):
    S.add(input())

count = 0
for _ in range(M):
    t = input()
    if t in S:
        count += 1
        
print(count)

# 성공