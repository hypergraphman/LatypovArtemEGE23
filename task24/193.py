line = open('24-191.txt').read()
words = line.split('A')
k = 0
for s in words:
    if s.find('B') + 1 >= 19:
        k += 1
print(k)