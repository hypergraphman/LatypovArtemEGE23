from itertools import product

alf = 'klrt'
for i, letters in enumerate(product(alf, repeat=4), start=1):
    if i == 67:
        print(letters)