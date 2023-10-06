string = input()
data = []
num = 0

for d in string:
    if d == "+" or d == "-":
        data.append(num)
        data.append(d)
        num = 0
    else: 
        num = num * 10 + int(d)
        # print(num)
data.append(num)

# print(data)

res = 0
state = 1
# 50-40+20-10+20
for s in data:
    if s == "+":
        s
    elif s == "-":
        state = 0
    else:
        if state == 1:
            res += s
        else: 
            res -= s

print(res)