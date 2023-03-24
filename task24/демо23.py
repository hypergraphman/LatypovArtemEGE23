s = open('24.txt').read()
s = s.replace('A', '*').replace('O', '*').replace('C', '?').replace('D', '?').replace('F', '?')
s = s.replace('?*', '0')
k = 0
mx = 0
for c in s:
    if c == '0':
        k += 1
        mx = max(k, mx)
    else:
        k = 0

print(mx)

data = s.replace('*', '?').split('?')
print(len(max(data)))