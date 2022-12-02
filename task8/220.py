from itertools import permutations

alf = 'sotkaplz'
k = 0
for lets in permutations(alf, r=5):
    word = ''.join(lets)
    if word.replace('a', 'o')[-1] != 'o' and 'zlo' not in word:
        k += 1
print(k)