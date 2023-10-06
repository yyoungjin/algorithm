import sys
input = sys.stdin.readline


n = int(input())
arr = []
stairs = []

for i in range(n):
    num = int(input())
    stairs.append(num)
    if i == 0:
        arr.append((num, num))
    elif i == 1:
        arr.append((num + arr[i-1][1], num))
    else:
        a = arr[i-1]
        b = arr[i-2]
        arr.append((num + a[1], num + max(b)))

print(max(arr[-1]))
# print(arr)