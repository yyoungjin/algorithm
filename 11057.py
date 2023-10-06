n = int(input())
data = [1]*10

for _ in range(0, n-1):
    tmp = [0] * 10
    for j in range(10):
        # for t in range(9, j-1, -1):
        #     tmp[t] = (tmp[t] + data[j]) % 10007
        tmp[j] = sum(data[j:]) % 10007

    data = tmp

print(sum(data)%10007)


