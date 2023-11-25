import sys
input = sys.stdin.readline
size=int(input())
ls=[*map(int, input().split())]
ls.sort()
save = 3000000001
ans=[]
for left in range(size-2):
    mid, right = left+1, size-1
    while mid<right:
        result=ls[left]+ls[mid]+ls[right]
        if abs(result)<save:
            save=abs(result)
            ans=[ls[left],ls[mid],ls[right]]
        if save==0: break
        if result<0: mid+=1
        else: right-=1
    if save==0: break
print(*ans)