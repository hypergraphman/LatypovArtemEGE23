def f(n):
    res = {1, n}
    for d in range(2, int(n**0.5) + 1):
        if n % d == 0:
            res.add(d)
            res.add(n // d)
    return sorted(res)


k = 0
for n in range(3159, 31585):
    if len(f(n)) == 2:
        k += n
print(k)
