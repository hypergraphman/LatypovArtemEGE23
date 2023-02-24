f = open('17-4.txt')
a = [int(x) for x in f.readlines()]

r = []
for i in a:
    if i % 25 == 6 and i % 16 == 9:
        r.append(i)

print(max(r), sum(r))