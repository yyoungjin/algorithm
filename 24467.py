data = []
count = 0
tmp = 0
while True:
    zeronum = input().count("0")
    if zeronum == 0:
        zeronum = 5
    tmp += zeronum
    data.append(tmp)

    # count 세주기
    if 0 < zeronum < 4:
        count+=1
        if count == 10:
            break

# 경로 찾기
if 5 in data:
    if 8 in data:
        if tmp > 11:
            print("WIN")
        else:
            print("LOSE")
    else:
        if tmp > 16:
            print("WIN")
        else:
            print("LOSE")
else: 
    if 10 in data:
        if tmp > 16:
            print("WIN")
        else:
            print("LOSE")
    else:
        if tmp > 20:
            print("WIN")
        else:
            print("LOSE")