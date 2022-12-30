line = '>' + '1' * 14 + '2' * 20 + '3' * 25
while '>1' in line or '>2' in line or '>3' in line:
    line = line.replace('>1', '22112>', 1)
    line = line.replace('>2', '2>', 1)
    line = line.replace('>3', '112>', 1)
print(sum(map(int, line[:-1])))
