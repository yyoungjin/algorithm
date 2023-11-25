# 27651
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

tmp = 0
sum_arr = []
for i in range(n):
    tmp += arr[i]
    sum_arr.append(tmp)


def part_sum(a, b):
    if a == 0:
        return sum_arr[b]
    return sum_arr[b] - sum_arr[a-1]


res = 0
p = n-1
ep = 2
for mp in range(1, n-1):
    head = sum_arr[mp-1]
    
    while head >= part_sum(p, n-1):
        p -= 1

    while part_sum(mp, ep-1) <= part_sum(ep, n-1):
        ep += 1

    if ep <= p and ep < n:
        res += (p - ep + 1)
    else: 
        break

print(res)