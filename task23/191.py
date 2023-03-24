def f(s, e):
    if s == e:
        return 1
    if s > e:
        return 0
    return f(s + 2, e) + f(s * 10 + 2, e)


print(f(2, 900))
