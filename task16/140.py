from functools import lru_cache
@lru_cache(None)
def f(n):
    if n > 10000:
        return n - 10000
    if n >= 1 and n <= 10000:
        return f(n+1) + f(n+2)


for i in range(10000, 1, -1):
    f(i)
print(f(12345)*(f(10) - f(12))/f(11) + f(10101))