# import sys
# input = sys.stdin.readline

# n = int(input())
# m = int(input())
# table = []
# visited = [False] * (n)
# for _ in range(n):
#     table.append(list(map(int,input().split())))

# plan = list(map(int, input().split()))

# def dfs(table, visited, citynum):
#     visited[citynum-1] = True
#     nextcity = 1
#     for r in table[citynum-1]:
#         if r == 1 and not visited[nextcity-1]:
#             dfs(table, visited, nextcity)
#         nextcity += 1

# dfs(table, visited, plan[0])

# res = "YES"
# for p in plan:
#     if not visited[p-1]:
#         res = "NO"

# print(res)

def solve():
    n = int(input())
    m = int(input())
    arr = []
    for _ in range(n):
        tmp = [int(x) for x in input().split()]
        arr.append(tmp)
    test = [int(x) - 1 for x in input().split()]
    rst = list(range(n))
    for i in range(n):
        for j in range(i+1, n):
            if arr[i][j] == 1:
                union(i, j, rst)
    pivot = find(test )
    