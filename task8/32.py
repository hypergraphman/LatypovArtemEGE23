from itertools import product

alf = 'abcd'
k = 0
for letters in product(alf, repeat=3):
    word = ''.join(letters)
    if ('a' not in word or ('aa' not in word and ('ad' in word or 'da' in word))) and ('bc' not in word and 'cb' not in word):
        k += 1
        print(word)
print(k)