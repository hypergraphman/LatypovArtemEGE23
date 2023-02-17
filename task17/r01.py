a = 0
b = 0
for i in range(1016,7938):
    if i % 3 == 0 and i % 7 != 0 and i % 17 != 0 and i % 19 != 0 and i % 27 != 0:
        a += 1
    if i > b:
        b = i
print(b)
print(a)