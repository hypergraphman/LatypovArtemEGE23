def f(s,e):
    if s == e:
        return 1
    if s > e:
        return 0
    return f(s + 1, e) + f(s + 2, e) + f(s + s + 1, e)


print(f(2, 10))
