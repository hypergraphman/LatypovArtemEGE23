def n_to_p(n, p):
    r = ''
    digits = '0123456789ABCDEF'
    while n > 0:
        r = digits[n % p] + r
        n //= p
    return r


for i in range(2, 10 + 1):
    print(n_to_p(432, i), i)