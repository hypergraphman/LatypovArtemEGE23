def f(s, e, k):
    if s == e:
        return 1
    if s > e:
        return 0
    return (f(s + 1, e, 1) if k != 1 else 0) + f(s + 2, e, 2) + f(s * 2, e, 3)


print(f(1, 18, 0))
