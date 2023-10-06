n = int(input())
arr = [list(input().split()) for _ in range(n)]

while (len(arr) != 1):
    num = int(arr[0][1])
    arr.pop(0)
    for _ in range(num - 1):
        temp = arr[0]
        arr.pop(0)
        arr.append(temp)
    arr.pop(0)
print(arr[0][0])


# import sys

# N = int(sys.stdin.readline())
# arr = [list(map(str, sys.stdin.readline().split())) for _ in range(N)]

# while(len(arr) != 1):
#     num = (int(arr[0][1]) - 1)  % (len(arr) - 1)
#     print(arr.pop(0))
    
#     for _ in range(num):
#         temp = arr[0]
#         arr.pop(0)
#         arr.append(temp)
#     print(arr.pop(0))
# print(arr[0][0])


# import sys
# from collections import deque
# n = int(input())
# data = deque()

# for _ in range(n):
#     p, id = sys.stdin.readline().rstrip().split()
#     data.append((p, int(id)))


# while len(data) > 1:
#     num = data.popleft()[1]
#     num %= len(data)
#     for _ in range(num):
#         data.append(data.popleft())

# print(data[0][0])