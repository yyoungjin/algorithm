# 22866

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

left_index = [] # 
left = [[0, -1000000] for _ in range(n)]
for i in range(n):
    if left_index:
        while left_index:
            if arr[left_index[-1]] <= arr[i]:
                left_index.pop()
            else:
                break
        if len(left_index):
            left[i] = (len(left_index), left_index[-1])
        left_index.append(i)
    else:
        left_index.append(i)

right_index = []
right = [[0, 1000000] for _ in range(n)]
for i in range(n-1, -1, -1):
    if right_index:
        while right_index:
            if arr[right_index[-1]] <= arr[i]:
                right_index.pop()
            else:
                break
        if len(right_index):
            right[i] = (len(right_index), right_index[-1])
        right_index.append(i)
    else:
        right_index.append(i)

for i in range(n):
    num = left[i][0]+right[i][0]
    if num == 0:
        print(0)
        continue
    if (i - left[i][1]) <= (right[i][1]-i):
        index = left[i][1]
    else:
        index = right[i][1]
    print(num, index + 1)