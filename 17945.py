b, c = map(int, input().split())
b = b+b

ans1 = ((-1) * b + (b*b - 4*c)**(1/2))/2
ans2 = ((-1) * b - (b*b - 4*c)**(1/2))/2
if ans1 < ans2:
    print(int(ans1), int(ans2))
elif ans1 == ans2:
    print(int(ans1))
else:
    print(int(ans2), int(ans1))