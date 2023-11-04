# 19637
import sys
input = sys.stdin.readline


def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        res = 0
        for tree in arr:
            if tree > mid:
                res+=(tree-mid)

        if res >= target:
            result = mid  # mid 값이 일단 저장됨
            start = mid + 1
        else:
            end = mid - 1
    
    return result


n, m = map(int, input().split())
arr = list(map(int, input().split()))

rst = binary_search(arr, m, 0, max(arr))
print(rst)
