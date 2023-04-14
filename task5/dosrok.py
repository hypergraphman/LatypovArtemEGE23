for n in range(1,1000):
    a = bin(n)[2:]
    if n % 3 == 0:
        a = a[-3:] + a
    else:
        a = bin(n%3*3)[2:] + a

    if int(a, 2) > 125:
        print(n)
