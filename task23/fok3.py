def f(s, e):
    if s > e or e == 22:
        return 0
    if s == e:
        return 1
    return f(s+1, e) + f(s*2, e)

print(f(1,10)*f(10,42))