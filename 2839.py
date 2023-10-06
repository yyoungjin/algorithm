n = int(input())

num = n%5
if num == 0:
    print(n//5)
elif num == (1 or 3):
    print(n//5 + 1)
elif num == 2:
    if n >= 12:
        print(n//5 + 2)
    else:
        print(-1)
elif num == 3:
    print(n//5+1)
else:
    if n == 4:
        print(-1)
    else:
        print(n//5+2)
