from itertools import product

alf = 'pirog'
k = 0
for i, letters in enumerate(product(alf, repeat=5), start=1):
    word = ''.join(letters)
    if (word.count('p') == 1 and (word.count('pi') + word.count('po') == 1) or
       word.count('p') == 2 and (word.count('pi') + word.count('po') == 2) or
       word.count('p') == 0):
        k += 1
        print(word)
print(k)