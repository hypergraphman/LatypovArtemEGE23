f = open('17-1.txt')
a = [int(x) for x in f.readlines()]

s = 0
for i in a:
    s += i
sr = s/len(a)
r = []
for p1,p2 in zip(a, a[1:]):
    if p1 < sr and p2 > sr or p1 > sr and p2 < sr:
        r.append(p1 + p2)

print(len(r), max(r))