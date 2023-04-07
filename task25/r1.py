def f(n):
    res = {1, n}
    for d in range(2, int(n**0.5) + 1):
        if n % d == 0:
            res.add(d)
            res.add(n // d)
    return sorted(res)

k = 1
for n in range(3532000, 3532161):
    if len(f(n)) == 2:
        print(k, n)
        k += 1