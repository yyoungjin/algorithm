a, b = map(int, input().split())
b += 1


def test(a):
    t = 2**61
    res = 0
    for i in range(60):
        t = t // 2
        if a // t:
            res += (a//t * (t//2))
            if a % t > (t//2):
                res += (a%t - (t//2))
        elif t//2 < a:
            res += (a - t//2)
    return res


print(test(b) - test(a))