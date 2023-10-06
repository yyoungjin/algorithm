#가중치 이용: 달 * 100 + 일수
tmp = [218, 320, 419, 520, 621, 722, 822, 922, 1022, 1122, 1221, 119]

memberlist = []
for _ in range(7):
    month, day = map(int, input().split())
    num = month*100 + day
    for i in range(12):
        if i == 11:
            if tmp[11] >= num or num > tmp[10]:
                memberlist.append(i)
        else:
            if tmp[i-1] < num <= tmp[i]:
                memberlist.append(i)

# print(memberlist)
# 신청자
apply = int(input())
applyList = []
for _ in range(apply):
    month, day = map(int, input().split())
    num = month*100 + day
    for i in range(12):
        if i == 11:
            if tmp[11] >= num or num > tmp[10]:
                if i not in memberlist:
                    applyList.append([month, day])
        else:
            if tmp[i-1] < num <= tmp[i]:
                if i not in memberlist:
                    applyList.append([month, day])

applyList.sort()
if len(applyList) == 0:
    print("ALL FAILED")
else:
    for birth in applyList:
        print(birth[0], birth[1])