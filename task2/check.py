for a in 0, 1:
    for b in 0, 1:
        f = int(a or not (a or b) or not a and b)
        print(f, end=' ')
print()
for a in 0, 1:
    for b in 0, 1:
        f = int(a or b or not a and not b)
        print(f, end=' ')
print()
for a in 0, 1:
    for b in 0, 1:
        f = int(True)
        print(f, end=' ')
print()