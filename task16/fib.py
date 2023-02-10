from functools import lru_cache


@lru_cache(None)
def f(n):
    if n <= 2:
        return 1
    if n > 2:
        return f(n - 1) + f(n - 2)


for i in range(1, 2000):
    f(i)
print(f(1000))
n = int(input())

a1 = 1
a2 = 1
for i in range(2, n + 1):
    a1, a2 = a2, a1 + a2
print(a1)
print(f(n))