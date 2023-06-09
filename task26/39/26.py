f = open('26-39.txt')
n, v = map(int, f.readline().split())
*a, = map(int, f.readlines())
a.sort(reverse=True)
k = 0
m = 0
for x in a:
    if 180<=x<=200:
        m += x
        k += 1
print(k,m)
v1 = v - m
print(v1)
a.sort()
for i in a:
    if v1 - i >=0:
        v1 -= i
        k += 1
print(k)