f = open('26-k6.txt')
n, k = map(int, f.readline().split())
r = []
for i in range(n):
    ves, price = map(int, f.readline().split())
    r.append((price / ves, ves))
r.sort(key=lambda x: (x[0], -x[1]))
print(r)
all_ves = 0
mx_ves = 0
mx_price = 0
for price, ves in r[:k]:
    all_ves += ves
    if ves > mx_ves:
        mx_ves = ves
        mx_price = price
print(all_ves, mx_ves * mx_price)