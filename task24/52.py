f = open('k8-4.txt').read()
k = 1
mx = 1
ans = []
for i in range(1, len(f)):
    if f[i-1] == f[i]:
        k += 1
        if k > mx:
            mx = k
            ans = [f[i]]
        elif k == mx:
            ans.append(f[i])
    else:
        k = 1
print(ans)
k = 1
for i in range(1, len(f)):
    if f[i-1] == f[i]:
        k += 1
        if k == mx:
            print(f[i], mx)
    else:
        k = 1

