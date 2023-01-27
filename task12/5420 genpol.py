mx_len = 0
mx_line = ''
for x in range(203 + 1):
    line = '1' * (203 - x) + '2' + '1' * (x)
    # print(line)
    while '111' in line or '222' in line:
        if '111' in line:
            line = line.replace('111', '22', 1)
        else:
            line = line.replace('222', '11', 1)
    if len(line) > mx_len:
        mx_len = len(line)
        mx_line = line
print(mx_line, mx_len)