from functools import lru_cache


@lru_cache(None)
def f(n):
    if n == 1:
        return 1
    if n > 1:
        return n * f(n-1)


s1 = int(input())
for i in range(1, s1):
    f(i)
print(f(s1))
a = 1
for i in range(1, s1+1):
    a *= i

print(a)