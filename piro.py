#20191
from bisect import bisect_left
# left_t에 해당 알파벳이 있는지 찾는게 우선.


#이분탐색
def b_search(d_i, t_i):
    start = 0
    end = len(dp[d_i]) - 1
    res = -1
    while start <= end:
        mid = (start + end) // 2
        if dp[d_i][mid] > t_i:
            res = mid
            end = mid - 1
        else:
            start = mid + 1

    return res

# input
s = list(input())
t = list(input())

dp = {i:[] for i in "abcdefghijklmnopqrstuvwxyz"}
for i in range(len(t)):
    dp[t[i]].append(i)

t_i = 0
res = 1
for i, w in enumerate(s):
    tmp = b_search(w, t_i) 
    tmp = bisect_left(dp[w], t_i)
    if tmp < len(dp[w]):
        t_i = dp[w][tmp]+1
    else:
        res += 1
        t_i = 0
        tmp = b_search(w, t_i) 
        if tmp < len(dp[w]):
            t_i = dp[w][tmp]+1
        else:
            print(-1)
            exit()

print(res)




# import sys
# input = sys.stdin.readline
# from bisect import bisect_left

# S = input().strip()
# T = input().strip()

# s,t = len(S),len(T)

# alphabet = {i:[] for i in "abcdefghijklmnopqrstuvwxyz"}
# for i in range(t):
#   alphabet[T[i]].append(i)

# cnt = 1
# last = 0
# for letter in S:
#   if not alphabet[letter]:
#     cnt = -1
#     break
#   idx = bisect_left(alphabet[letter],last)
#   if idx == len(alphabet[letter]):
#     cnt += 1
#     last = 0
#     idx = bisect_left(alphabet[letter],last)
#   last = alphabet[letter][idx]+1

# print(cnt)