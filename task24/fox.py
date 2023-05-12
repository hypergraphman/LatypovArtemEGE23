s = open('24.txt').read()

# print(s1) # 14
mx = 16
t = {'FEG', 'GEF'}
k = 0
for i in range(4, len(s), 3):
    p1, p2, p3 = s[i - 2], s[i - 1], s[i]
    if p1 + p2 + p3 in t:
        k += 1
        if k > mx:
            mx = k
    else:
        k = 0
print(mx)