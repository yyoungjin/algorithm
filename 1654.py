k, n = map(int, input().split())
data = []

for _ in range(k):
    data.append(int(input()))

start = 0
end = max(data) + 1

while end - start > 1:
    count = 0
    mid = (start+end)//2
    for i in data:
        count += i//mid
    if count < n:
        end = mid
        res = end
    else:
        start = mid
        res = mid

print(start)