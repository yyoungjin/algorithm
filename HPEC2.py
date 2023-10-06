num = int(input())
num //= 4763

# x 는 국+수, y 는 영+탐

tmp = [i for i in range(201)]
data = []

for i in tmp:
    for j in tmp:
        if abs(i * 508 + j * 212) == num:
            data.append((i, j))
        if abs(i * 108 + j * 212) == num:
            data.append((i, j))
        if abs(i * 508 + j * 305) == num:
            data.append((i, j))
        if abs(i * 108 + j * 305) == num:
            data.append((i, j))

print(len(data))
if len(data) != 0:
    data.sort(key = lambda x: (x[0], x[1]))
    for i in data:
        print(i[0], i[1])

