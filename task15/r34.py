for a in range(1, 100):
    is_a = True
    for n in range(1, 100):
        for k in range(1, 100):
            if not ((5 * k + 6 * n > 57) or ((k <= a) and (n < a))):
                is_a = False
    if is_a:
        print(a)
               