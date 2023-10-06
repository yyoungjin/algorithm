# 26150
num = int(input())
result = []
strlist = []
for _ in range(num):
    strlist.append(input().split())
strlist.sort(key=lambda x: int(x[1]))
for string in strlist:
    D = int(string[2])
    result.append(string[0][D-1].upper())
print("".join(result))
    
