n, k = map(int, input().split())
data = list(map(int, input().split()))

sorted(data)
group = [0] * k
while data:
    for j in range(k):
        group[j]