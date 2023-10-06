table = {}
table[0] = 0
for i in range(1, 10):
    table[i] = 1
n = int(input())
for j in range(2, n+1):
    data = []
    for t in range(10):
        if t == 0:
            data.append(table[1])
        elif t<9:
            data.append((table[t-1] + table[t+1])%1000000000)
        else:
            data.append(table[8])
    for i in range(10):
        table[i] = data[i]

print(sum(list(table.values()))%1000000000)