f = open('17-338.txt')
a = [int(x) for x in f.readlines()]

mn = min(a)

r = []
for p1, p2 in zip(a, a[1:]):
   if p1 % 117 == mn or p2 % 117 == mn:
       r.append(p1 + p2)
print(len(r), max(r))