import sys
from collections import deque

t = int(input())
ans = []
for i in range(t):
    p = sys.stdin.readline().rstrip()
    n = int(input())
    arr = sys.stdin.readline().rstrip()[1:-1].split(",")
    queue = deque(arr)

    rev, front, back = 0, 0, len(queue)-1
    flag = 0
    if n == 0:
        queue = []
        front = 0
        back = 0

    for j in p:
        if j == 'R':
            rev += 1
        elif j == 'D':
            if len(queue) < 1:
                flag = 1
                ans.append("error")
                break
            else:
                if rev % 2 == 0:
                    queue.popleft()
                else:
                    queue.pop()
    if flag == 0:
        if rev % 2 == 0:
            ans.append("[" + ",".join(queue) + "]")
        else:
            queue.reverse()
            ans.append("[" + ",".join(queue) + "]")

for a in ans:
    print(a)