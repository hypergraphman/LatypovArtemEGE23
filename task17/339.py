f = open('17-339.txt')
a = [int(x) for x in f.readlines()]

mn = 10**10
for x in a:
    if x > 0 and x % 19 == 0 and x < mn:
        mn = x

r = []
for p1, p2 in zip(a, a[1:]):
    if p1 + p2 < mn:
        r.append(p1 + p2)
print(len(r), max(r))