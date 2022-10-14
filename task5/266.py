def alg(n):
    if n % 3 == 0:
        s1 = n // 3
    else:
        s1 = n - 1
    if s1 % 5 == 0:
        s2 = s1 // 5
    else:
        s2 = s1 - 1
    if s2 % 11 == 0:
        s3 = s2 // 11
    else:
        s3 = s2 - 1
    return s3


c = 0
for i in range(2, 10000):
    if alg(i) == 8:
        c += 1
print(c)