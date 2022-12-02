from itertools import product

alf = 'oprt'
for i, letters in enumerate(product(alf, repeat=5), start=1):
    word = ''.join(letters)
    if word == 'ropot' or word == 'topor':
        print(i)


