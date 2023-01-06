c = 0
a = (7 ** 80 - 7 ** 4 + int('234', 7)) * 5 * 8 // 6
while a > 0:
    if a % 7 == 4:
        c += 1
    a //= 7
print(c)
