# 2515
import sys
input = sys.stdin.readline

n, s = map(int, input().split())
heights = []
prices = {}
for _ in range(n):
    h, p = map(int, input().split())
    if h < s:
        continue
    if h in prices:
        prices[h] = max(prices[h], p)
    else:
        prices[h] = p
        heights.append(h)

heights.sort()

def find_p(x): # 높이가 x 보다 작거나 같은 그림 중 가장 큰 그림의 가격을 찾아라
    start = 0
    end = len(heights)
    res = 0
    while start<=end:
        mid = (start + end) // 2
        if heights[mid] <= x:
            res = prices[heights[mid]]
            start = mid + 1
        else:
            end = mid - 1
        
    return res


# dp[x]는 dp[x-1]과 dp[x-s]+(높이가 x인 그림가격) 중 큰 값이다.
for i, l in enumerate(heights): 
    # l-s 이하 중 가장 큰 그림을 찾는게 핵심
    if i == 0:
        continue
    prices[l] = max(prices[heights[i-1]], find_p(l-s) + prices[l])

print(prices[l])