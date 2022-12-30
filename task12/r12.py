
for x in range(10 + 1):
    a = '21' * x + (10 - x) * '1'
    while '21' in a:
        a = a.replace('21', '5', 1)

    if sum(map(int, a)) == 34:
        print(x)