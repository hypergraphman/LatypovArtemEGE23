res = []
for x in '0123456789ABCDEF':
    for y in '0123456789ABCDEF':
        n = f'1{x}DED{y}BABA'
        if int(n, 16) % (11 * 16 + 10) == 0:
            res.append((int(n, 16), int(n, 16) // (11 * 16 + 10)))
print(*sorted(res)[::-1], sep='\n')

