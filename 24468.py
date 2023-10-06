# input
L, N, T = map(int, input().split())

dtlist = []
drlist = []
count = 0

for _ in range(N):
    dt, dr = input().split()
    dtlist.append(int(dt))
    drlist.append(dr)


# 시간을 기준으로 반복문 실행, t초 후 상황
for t in range(1, T+2):
    result = []
    # 부딪힐 공이 있는 지 판단
    for n in range(N):
        if dtlist.count(dtlist[n]) > 1:
            result.append(n)
    for i in range(N):
        # 1. 벽 부딪치기
        if dtlist[i] == L or dtlist[i] == 0:
            if drlist[i] == "L":
                drlist[i] = "R"
                dtlist[i] = dtlist[i]+1
            else:
                drlist[i] = "R"
                drlist[i] = "L"
                dtlist[i] = dtlist[i]-1

        # 2. 공 부딪치기
        elif i in result:
            count += 1
            if drlist[i] == "L":
                drlist[i] = "R"
                dtlist[i] = dtlist[i]+1
            else:
                drlist[i] = "R"
                drlist[i] = "L"
                dtlist[i] = dtlist[i]-1

        # 3. 아무일 없이 진행
        else:
            if drlist[i] == "L":
                dtlist[i] = dtlist[i]-1
            else:
                drlist[i] = "R"
                dtlist[i] = dtlist[i]+1

print(int(count//2))