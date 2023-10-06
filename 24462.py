from itertools import combinations
import math

# input
N, D = map(int, input().split())
T = []
K = []
count = []

for _ in range(N):
    Tt, Kk = map(int, input().split())
    T.append(Tt)
    K.append(Kk)

# count
for i in range(N):
    t = T[i]
    k = K[i]

    # 식
    if t == 0:
        count.append(D // k + 1)
    else:
        count.append((D // k + 1) - (t // k))
# print(count)


# 조합생성
comblist = list(combinations(range(N), 2))
data = []
for comb in comblist:
    combK = math.lcm(K[comb[0]], K[comb[1]])

    if T[comb[0]] == 0 and T[comb[1]] == 0:
        combocount = (D // combK + 1)
    else:
        combT = max(T[comb[0]], T[comb[1]], combK)
        # 콤비네이션의 시작점이 최소공배수가 아닐 수 있음!!!
        if combT % combK != 0:
            combT = combT+(combK - combT % combK)
        combocount = (D // combK + 1) - (combT // combK)
    
    res = count[comb[0]] + count[comb[1]] - combocount
    # print(count[comb[0]], count[comb[1]], combocount)
    data.append([comb[0], comb[1], res])

# print(data)

# 최댓값찾기
maxnum = 0
maxindex = 0
for d in range(len(data)):
    if maxnum < data[d][2]:
        maxindex = d
        maxnum = data[d][2]
# print(maxindex)

#print
print(data[maxindex][0]+1, data[maxindex][1]+1)
print(data[maxindex][2])