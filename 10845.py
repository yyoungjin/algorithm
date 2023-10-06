from collections import deque

queue = deque()

n = int(input())
res = []
for _ in range(n):
    s = input()
    if s[:4] == 'push':
        a, b = s.split()
        queue.append(int(b))
    elif s[:3] == 'pop':
        if len(queue) == 0:
            res.append(-1)
        else:
            res.append(queue.popleft())
    elif s[:4] == 'size':
        res.append(len(queue))
    elif s[:5] == 'empty':
        if len(queue) == 0:
            res.append(1)
        else:
            res.append(0)
    elif s[:5] == 'front':
        if len(queue) == 0:
            res.append(-1)
        else:
            res.append(queue[0])
    elif s[:4] == 'back':
        if len(queue) == 0:
            res.append(-1)
        else:
            res.append(queue[-1])

for d in res:
    print(d)
