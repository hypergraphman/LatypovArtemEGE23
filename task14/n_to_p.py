from string import digits, ascii_uppercase


def n_to_p(n, p):
    r = ''
    #         0123456789012345
    digits = '0123456789ABCDEF'
    # digits = digits + ascii_uppercase
    while n > 0:
        r = digits[n % p] + r
        n //= p
    return r


print(n_to_p(255, 16))  # FF
print(n_to_p(194, 5))  # 1234
print(n_to_p(10, 2))  #1010

print(n_to_p(4**2016 - 2**2018 + 8**800 - 80, 2).count('1'))

print(n_to_p(16, 6))