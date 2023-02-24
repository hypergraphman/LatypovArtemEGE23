f = open('17-9.txt')
a = [int(x) for x in f.readlines()]

r =[]

for p1,p2,p3 in zip(a,a[1:], a[2:]):
    c = 0

    bp1 = bin(p1)[2:]
    if bp1.count('1') == 2 and bp1.count('0') >= 1:
        c += 1

    bp2 = bin(p2)[2:]
    if bp2.count('1') == 2 and bp2.count('0') >= 1:
        c += 1

    bp3 = bin(p3)[2:]
    if bp3.count('1') == 2 and bp3.count('0') >= 1:
        c += 1

    if c >= 2:
        r.append(max(p1,p2,p3))
print(len(r), sum(r))