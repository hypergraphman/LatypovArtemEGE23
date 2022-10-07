def alg(n):
    s1 = f'{n:b}'
    s2 = s1[1:].lstrip('0')
    if not s2:
        s2 = '0'
    s3 = int(s2, 2)
    s4 = n - s3
    return s4


print(alg(2000))

a = set()
for i in range(500, 5000 + 1):
    a.add(alg(i))
print(len(a))
