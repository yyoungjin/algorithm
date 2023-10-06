t = int(input())
data = [0,0,0,0,0]
tmp = list(map(int, input().split()))

for i in range(t):
    data[i] = tmp[i]


res = 0
if data[0] > data[2]:
    res += abs(data[0] - data[2]) * 508
else:
    res += abs(data[0] - data[2]) * 108


if data[1] > data[3]:
    res += abs(data[1] - data[3]) * 212
else:
    res += abs(data[1] - data[3]) * 305

res += data[4] * 707


print(res*4763)

