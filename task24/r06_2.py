s = open('k8.txt').read()
k = 1
mx = 1
res = [s[0]]
for i in range(1, len(s)):
    if s[i - 1] == s[i]:
        k += 1
        if k > mx:
            mx = k
            res = [s[i]]
        if k == mx:
            res.append(s[i])
    else:
        k = 1
print(mx, res)