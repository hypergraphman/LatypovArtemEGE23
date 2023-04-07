from functools import lru_cache


@lru_cache(None)
def f(n):
    res = set()
    for d in range(2, int(n**0.5) + 1):
        if n % d == 0:
            res.add(d)
            res.add(n // d)
    return sorted(res)


for n in range(174457, 174506):
    if len(f(n)) == 2:
        print(*f(n))


