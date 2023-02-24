f = open('17-3.txt')
a = [int(x) for x in f.readlines()]

r = []
for p1,p2,p3 in zip(a,a[1:],a[2:]):
    if p1 < p2 < p3:
        r.append(p3 - p1)

print(len(r), min(r))