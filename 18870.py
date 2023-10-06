n = int(input())
arr = list(map(int, input().split()))

arr2 = sorted(list(set(arr)))

dic = {arr2[i] : i for i in range(len(arr2))}

res = []
for j in arr:
    res.append(str(dic[j]))

print(' '.join(res))

# 성공
