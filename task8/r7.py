from itertools import product
alf = 'vesna'
k = 0
for letters in product(alf, repeat=3):
    if 'a' in letters:
        k += 1
print(k)