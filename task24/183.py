line = open('24-181.txt').readline()
words = line.split('.')
lens = []
for word in words:
    lens.append(len(word))

mx = 0
for p1, p2, p3, p4 in zip(lens,lens[1:], lens[2:], lens[3:]):
    mx = max(mx, p1 + p2 + p3 + p4)
print(mx + 3)