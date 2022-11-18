from itertools import product

alf = 'егэ'
k = 0
for letters in product(alf, repeat=5):
    if letters[0] in 'еэ':
        k += 1
print(k)
