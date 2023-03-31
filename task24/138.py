f = open('24-s1.txt')
k = 0
for line in f.readlines():
    char_k = char_u = 0
    for char in line:
        if char == 'K':
            char_k += 1
        if char == 'U':
            char_u += 1
    if char_k > char_u:
        k += 1
print(k)