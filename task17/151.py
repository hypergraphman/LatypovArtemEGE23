f = open ('17-1.txt')
a = [int(x) for x in f.readlines()]

r = []
for p1, p2 in zip(a, a[1:]):
    if abs(p1) % 10 == 6 and p1 % 3 == 0 or abs(p2) % 10 == 6 and p2 % 3 == 0:
        r.append(min(p1, p2))

print(len(r), min(r))
