f = open('24.txt').read()
f = f.replace('A', '?').replace('E', '?').replace('O', '?').replace('B', '*').replace('C', '*').replace('D', '*')
f = f.replace('?*', '!')
k = 1
mx = 1
for i in f:
    if i == '!':
        k += 1
        mx = max(k, mx)
    else:
        k = 0
print(mx)




