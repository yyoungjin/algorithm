def mod(n, c, mod):
    res = 1

    n % mod
    if n  == 0:
        return 0
    
    while c > 0:
        if c % 2 == 1:
            res = (res*n) % mod
        c//=2
        n = (n*n) % mod
        
    return res