from itertools import product
alf = 'слон'
k = 0
for letters in product(alf, repeat=5):
    if letters.count('с') == 1:
        k += 1
print(k)