def f(s, k):
    if k == 13:
        res.add(s)
        return None
    f(s + 3, k + 1)
    f(s * 2 + 1, k + 1)


res = set()
f(2, 0)
print(len(res))
