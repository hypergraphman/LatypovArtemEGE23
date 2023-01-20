for a in range(1, 1000):
    is_a = True
    for x in range(1, 1000):
        xnda = x % a != 0
        xd6 = x % 6 == 0
        xnd9 = x % 9 != 0
        if not (xnda <= (xd6 <= xnd9)):
            is_a = False
    if is_a:
        print(a)


for a in range(1, 1000):
    if all((x % a != 0) <= ((x % 6 == 0) <= (x % 9 != 0)) for x in range(1, 1000)):
        print(a)