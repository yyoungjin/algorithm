

n = int(input())
s = input()
d, m = map(int, input().split())
hyu = {'H':0, 'Y':0, 'U':0}

num = (d + m) // d # num개 까지는 그냥 지우는게 빠름

count = 0
res = 0
us = False
for i in s:
    if (i == 'H') or (i == 'Y') or (i == 'U'):
        us = True
        hyu[i] = hyu[i] + 1
        if count != 0:
            if count > num:
                res += (d+m)
            else:
                res += (count * d)
        count = 0
        continue
    else:
        count += 1

if count != 0:
    if count > num:
        res += (d+m)
    else:
        res += (count * d)
    





nc = 1e9
for j in hyu.values():
    nc = min(nc, j)

if res == 0:
    print('Nalmeok')
else:
    print(res)
    
if nc == 0:
    print("I love HanYang University")
else:
    print(nc)