from itertools import product

for i, letters in enumerate(product('АКЛМНЯ', repeat = 5), start = 1):
    word = ''.join(letters)
    if word[0] == 'К' and word[1] == 'М':
        print(i)
        break