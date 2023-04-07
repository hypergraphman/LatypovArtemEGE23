from functools import lru_cache


@lru_cache(None)
def f(n):
    res = {1,n}
    for d in range(2, int(n**0.5) + 1):
        if n % d == 0:
            res.add(d)
            res.add(n // d)

    return sorted(res)


ms = 10**10
find_n = 0
for n in range(573213, 575341):
    if len(f(n)) == 4 and sum(f(n)) < ms:
        ms = sum(f(n))
        find_n = n
print(ms, f(find_n)[-2])
