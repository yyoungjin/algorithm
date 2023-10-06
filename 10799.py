import sys

N = int(sys.stdin.readline())
line = sys.stdin.readline().rstrip()
D, M = map(int, sys.stdin.readline().split())
cnt = 0
energy = 0
ans = [0, 0, 0]
for i in line:
    if i != 'H' and i != 'Y' and i != 'U':
        cnt += 1
    else:
        if cnt == 1:
            energy += D
            cnt = 0
        elif cnt > 1:
            energy += D + M
            cnt = 0
        if i == 'H':
            ans[0] += 1
        elif i == 'Y':
            ans[1] += 1
        elif i == 'U':
            ans[2] += 1
if cnt == 1:
    energy += D
elif cnt > 1:
    energy += D + M

if res == 0:
    print('Nalmeok')
else:
    print(res)
    
if nc == 0:
    print("I love Hanyang University")
else:
    print(nc)