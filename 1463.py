n = int(input())

data = [0] * (n+4)
data[1] = 0
data[2] = 1
data[3] = 1
for x in range(4, n+4):
    if x % 6 == 0:
        data[x] = min(data[x//3], data[x//2], data[x-1]) + 1
    elif x % 3 == 0:
        data[x] = min(data[x//3], data[x-1]) + 1
    elif x % 2 == 0:
        data[x] = min(data[x//2], data[x-1]) + 1
    else:
        data[x] = data[x-1] + 1

print(data[n])