line = open('24-181.txt').readline()
words = line.split('.')
lens = []

for word in words:
    if word.count('A') >= 3:
        lens.append(len(word))
print(max(lens))