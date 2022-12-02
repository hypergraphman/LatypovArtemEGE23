from itertools import product

alf = 'geroy'
k = 0
for lets in product(alf, repeat=4):
    word = ''.join(lets)
    if word[0] != 'y' and word.count('e') + word.count('o') >= 1:
        k += 1
print(k)
k = 0
for lets in product(alf, repeat=4):
    word = ''.join(lets)
    if word[0] != 'y' and ('e' in word or 'o' in word):
        k += 1
print(k)
k = 0
for lets in product(alf, repeat=4):
    word = ''.join(lets).replace('o', 'e')
    if word[0] != 'y' and word.count('e') >= 1:
        k += 1
print(k)