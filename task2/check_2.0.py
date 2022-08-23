def f1(a, b):
    return int(a <= b)


def f2(a, b):
    return int(not a or b)


print('a b 1 2')
for a in 0, 1:
    for b in 0, 1:
        print(a, b, f1(a, b), f2(a, b))