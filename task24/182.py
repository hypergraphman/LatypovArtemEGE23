line = open('24-181.txt').readline()
words = line.split('.')
print(words)
lens = []
for word in words:
    lens.append(len(word))
print(lens)
mx = 0
for p1, p2, p3 in zip(lens,lens[1:], lens[2:]):
    mx = max(mx, p1 + p2 + p3)
print(mx + 2)