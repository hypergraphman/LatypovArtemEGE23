from itertools import permutations

alf = 'uley'
k = 0
for letters in permutations(alf):
    word = ''.join(letters)
    if word[0] != 'y' and 'eu' not in word:
        k += 1
print(k)