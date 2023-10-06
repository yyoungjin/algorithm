# N = int(input())
# result = 0

# def dfs(rooom, day):
#     global result
#     if day >= N:
#         result += 1
#         return
#     day += 1
#     # print("day", day)
#     if day == 1:
#         for room in [0,1,2,3,4]:
#             dfs(room, day)

#     else:
#         if rooom == 0:
#             for room in [1,2,3,4]:
#                 dfs(room, day)
#         elif rooom == 1 or rooom == 4:
#             for room in [0, 3, 4]:
#                 dfs(room, day)
#         else:
#             for room in [0, 1]:
#                 dfs(room, day)
#     return result

# ans = dfs(0, 0) % 1000000007
# print(ans)


# 2차 시도
# 1. 첫째날 경우의 수 1, 2, 2
# 2. 2날은 4, 6, 4
# 3. 10, 18, 14
# 4. 32, 
N = int(input())
result = 0
one = 1
two = 2
three = 2

for n in range(2, N+1):
    a = one
    b = two
    c = three
    one = (b+c)%1000000007
    two = (a * 2 + b + c)%1000000007
    three = (a * 2 + b)%1000000007
result = one + two + three
result = result % 1000000007
print(result)

"""
64비트 이상이면 연산 처리 속도 급격히 느려짐

"""