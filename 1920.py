n = int(input())
data = list(map(int, input().split()))
dic = {}
for i in data:
    dic[i] = 1

m = int(input())
cases = list(map(int, input().split()))
for j in cases:
    try:
        print(dic[j])
    except:
        print(0)