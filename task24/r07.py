s = open('24.txt').read()

k = 1
mx = 1
for i in range(1, len(s)):
    if s[i - 1] != s[i]:
        k += 1
        mx = max(k, mx)
    else:
        k = 1
print(mx)