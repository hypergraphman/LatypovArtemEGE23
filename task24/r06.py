s = open('k8.txt').read()
k = 1
mx = 1
for i in range(1, len(s)):
    if s[i - 1] == s[i]:
        k += 1
        mx = max(k, mx)
    else:
        k = 1
print(mx)
k = 1
for i in range(1, len(s)):
    if s[i - 1] == s[i]:
        k += 1
        if k == mx:
            print(s[i])
    else:
        k = 1