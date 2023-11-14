#19623
import sys
import bisect
input = sys.stdin.readline

"""
end 가 해당 좌표인 객체를 아는 것이 핵심
 -> key가 좌표, value는 해당 좌표가 end 값인 객체
"""
n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

# 좌표압축
tmp = set()
for d in data:
    tmp.add(d[0])
    tmp.add(d[1])
c = list(tmp)
c.sort()

# 이 값의 좌표를 알려줘
find_i = {}
for i, v in enumerate(c):
    find_i[v] = i

# key가 좌표, value는 해당 좌표가 end 값인 객체 저장
find_class = {}
for lesson in data:
    # end의 좌표 찾기
    idx = bisect.bisect_left(c, lesson[1])
    if idx in find_class:
        find_class[idx] = find_class[idx].append(lesson)
    else:
        find_class[idx] = [lesson]    

# 좌표 별 dp 생성
dp = [0] * len(c)
for i in range(1, len(c)):
    if i in find_class:
        for lesson in find_class[i]:
            dp[i] = max(dp[i-1], dp[find_i[lesson[0]]] + lesson[2], dp[i])
    else:
        dp[i] = dp[i-1]

print(dp[-1])