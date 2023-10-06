import sys
input = sys.stdin.readline

N = int(input())

S = []
A = []

for _ in range(N):
    tmp = input()
    if tmp[0] == "1":
        a, b = map(int, tmp.split())
        S.append(b)
    else:
        q = int(tmp)
        if q == 2:
            if S:
                A.append(S.pop())
            else:
                A.append(-1)
            
        elif q == 3:
            A.append(len(S))
        elif q == 4:
            if S:
                A.append(0)
            else:
                A.append(1)
        else:
            if S:
                A.append(S[-1])
            else:
                A.append(-1)

for ans in A:
    print(ans)