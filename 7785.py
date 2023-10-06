n = int(input())
s = {}

for _ in range(n):
    name, stance = input().split()
    if stance == "enter":
        s[name] = stance
    else: 
        del s[name]

s = sorted(s.keys(), reverse = True)

for ss in s:
    print(ss)