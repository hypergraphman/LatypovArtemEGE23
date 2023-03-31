f = open('24-s1.txt')
answer = 0
for s in f.readlines():
    k = 0
    for i in range(0, len(s) - 2):
        if s[i] == 'A' and s[i + 2] == 'R':
            k = 1
    answer += k
print(answer)
