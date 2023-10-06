from collections import deque
n = int(input())
data = deque()

for _ in range(n):
    p, id = sys.stdin.readline().rstrip().split()
    data.append((p, int(id)))


while len(data) > 1:
    num = data.popleft()[1]
    num %= len(data)
    for _ in range(num):
        data.append(data.popleft())

print(data[0][0])