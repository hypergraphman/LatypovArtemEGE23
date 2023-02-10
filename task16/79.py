from functools import lru_cache


@lru_cache(None)
def f(n):
    if n <= 5:
        return n
    if n > 5 and n % 3 == 0:
        return n + f(n//3 + 1)
    if n > 5 and n % 3 != 0:
        return 100000000


for i in range(1, 1000):
    f(i)

i = 1
while not (1000 < f(i) < 100000000):
    i += 1
print(i)