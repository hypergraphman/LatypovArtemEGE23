def f(n):
    res = {1, n}
    for d in range(2, int(n**0.5) + 1):
        if n % d == 0:
            res.add(d)
            res.add(n // d)
    return sorted(res)
k = 0
for n in range(2532000, 2532161):
    if len(f(n)) == 2:
        k += 1
        if k % 3 == 1:
            print(k,n)