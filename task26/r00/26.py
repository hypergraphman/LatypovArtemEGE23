f = open('26.txt')
v, n = map(int, f.readline().split())
*a, = map(int, f.readlines())
a.sort()
k = 0
p = 0
last = 0
for i in a:
    if k + i <= v:
        k += i
        p += 1
        last = i
print(p)
k -= last
d = v - k
mx = 0
for x in a:
    if x < 70 and x > mx:
        mx = x
print(mx)
