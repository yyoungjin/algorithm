import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
B.sort()

C = []

for i in range(n):
    if i > (m-1):
        print(B[0])
    else:
        start = 0
        end = m-1
        a = A[i]
        tmp = 1e9
        while start < end: # end는 미포함
            mid = (start + end) // 2
            newtmp = abs(B[mid] - a)
            if B[mid] < a:
                start = mid+1
                if newtmp < tmp:
                    tmp = newtmp
                else:
                    break
            else:
                end = mid
                if newtmp < tmp:
                    tmp = newtmp
                else:
                    break

        print(B[start])