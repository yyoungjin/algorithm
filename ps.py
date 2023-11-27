import sys

def palindrome(s, res):
    sp, ep = 0, len(s)-1
    while sp < ep:
        if s[sp] == s[ep]:
            sp += 1
            ep -= 1
        elif not res:
            if palindrome(s[sp+1:ep+1], 1) == 0:
                return 1
            elif palindrome(s[sp:ep], 1) == 0:
                return 1
            else:
                return 2

        else:
            return 2
        
    return 0


n = int(sys.stdin.readline())
res = []
for _ in range(n):
    s = list(sys.stdin.readline().rstrip())
    res.append(palindrome(s, 0))

for i in res:
    print(i)