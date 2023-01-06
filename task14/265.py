def n_to_p(n, p):
    r = ''
    digits = '0123456789ABCDEF'
    while n > 0:
        r = digits[n % p] + r
        n //= p
    return r


s = n_to_p(26**2+169-11, 13)
print(s.count('2') + s.count('C'))