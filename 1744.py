n = int(input())
plus = []
minus = []

zerocount = 0
onecount = 0
for _ in range(n):
    num = int(input())
    if num == 0:
        zerocount += 1
    elif num == 1:
        onecount += 1
    elif num > 1:
        plus.append(num)
    else:
        minus.append(num)

if len(plus) % 2 == 1:
    plus.append(1)
if len(minus) % 2 == 1:
    if zerocount > 0:
        minus.append(0)
    else:
        minus.append(1)

plus.sort()
minus.sort(reverse=True)

res = 0
for _ in range(len(plus)//2):
    num1 = plus.pop()
    num2 = plus.pop()
    res += num1 * num2

for _ in range(len(minus)//2):
    num1 = minus.pop()
    num2 = minus.pop()
    res += num1 * num2

res += onecount


print(res)


