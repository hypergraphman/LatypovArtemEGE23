def dva(a):
    for i in range(len(a)):
        a[i] = 2 * a[i]


def new_dva(a):
    new_a = []
    for n in a:
        new_a.append(2 * n)
    return new_a


b = [1, 2, 3]
c = new_dva(b)
print(b)
print(c)
dva(c)
print(c)
