def alg(n):
    s1 = f'{n:b}'
    if n % 2 == 0:
        s2 = '1' + s1 + '10'
    else:
        s2 = '11' + s1 + '0'
    r = int(s2, 2)
    return r


print(alg(13))

a = set()
for i in range(1, 10000):
    t = alg(i)
    if 800 <= t <= 1500:
        a.add(t)
print(len(a))
