# 17404
INF = 1e9
n = int(input())
rgb = []
ans = INF
for _ in range(n):
    rgb.append(list(map(int, input().split())))

for i in range(3):
    pdp = [INF, INF, INF]
    pdp[i] = rgb[0][i]
    for j in range(1, n):
        dp = rgb[j][:]
        dp[0] = rgb[j][0] + min(pdp[1], pdp[2])
        dp[1] = rgb[j][1] + min(pdp[0], pdp[2])
        dp[2] = rgb[j][2] + min(pdp[0], pdp[1])
        pdp = dp

    for j in range(3):
        if i != j:
            ans = min(ans, dp[j])
print(ans)