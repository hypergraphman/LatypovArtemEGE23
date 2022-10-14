def alg(n):
    s1 = f'{n:b}'
    if '0' not in s1:
        return -1
        # raise Exception("Алгоритм аварийно завершён")
    else:
        i = s1.rfind('0')
        s2 = s1[:i] + s1[:2] + s1[i + 1:]
    s3 = s2[::-1]
    s4 = int(s3, 2)
    return s4


i = 2
while alg(i) != 123:
    i += 1
print(i)