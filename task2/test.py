from itertools import product

print('x y z w f')
f1 = []
f2 = []
for x, y, z, w in product([0, 1], repeat=4):
    f_origin = x or not w or (y != z) and (y <= z)
    f_my_ans = x or not w or (y != z) or (y <= z)
    f1.append(int(f_origin))
    f2.append(int(f_my_ans))
print(*f1)
print(*f2)
if f1 == f2:
    print('yes')