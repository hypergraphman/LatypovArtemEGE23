def alg(n):
    str_n = str(n)
    d2, d1, d0 = str_n[0], str_n[1], str_n[2]
    a = [int(d2 + d1), int(d1 + d2), int(d2 + d0), int(d0 + d2), int(d1 + d0), int(d0 + d1)]
    b = []
    for el in a:
        if 10 <= el <= 99:
            b.append(el)
    return max(b) - min(b)


i = 100
while alg(i) != 40:
    i += 1
print(i)
