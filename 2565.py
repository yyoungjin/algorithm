# import sys
# input = sys.stdin.readline

# n = int(input())
# table = {}
# data = [[] for _ in range(101)]

# for _ in range(n):
#     a, b = map(int, input().split())
#     table[a] = b
#     for t in table.keys():
#         if t == a:
#             continue
#         if (a-t) * (table[a] - table[t]) < 0:
#             data[a].append(t)
#             data[t].append(a)

# count = 0
# while True:
#     tmp = 0
#     res = 0
#     for i in range(len(data)):
#         if len(data[i]) > tmp:
#             res = i
#             tmp = len(data[i])
#     if tmp == 0:
#         break
#     for d in data[res]:
#         data[d].remove(res)
#     data[res] = []
#     count += 1

# print(count)


#lis 알고리즘!!!!!!!!!!!!!

import sys
input = sys.stdin.readline


def lis(arr, n):
    rst = [1] * n
    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i]:
                rst[i] = max(rst[i], rst[j] + 1)
    return max(rst)

def solve():
    n = int(input())
    arr = []
    for _ in range(n):
        a, b = map(int, input().split())
        arr.append((a, b))
    arr.sort(key = lambda x : x[0])
    l = []
    for a, b in arr:
        l.append(b)
    print(n - lis(l, n))

solve()