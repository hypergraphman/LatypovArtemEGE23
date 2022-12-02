from itertools import product
alf = 'komar'
k = 0
for letters in product(alf, repeat=4):
    if letters.count('a') <= 3:
        k += 1
print(k)