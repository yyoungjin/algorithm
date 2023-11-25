#27648
n, m, k = map(int, input().split())
if (n+m-1) > k:
    print("NO")
    exit()

else:
    print("YES")
    for i in range(n):
        print(' '.join(map(str, [i+j+1 for j in range(m)])))