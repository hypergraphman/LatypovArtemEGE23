from fnmatch import *
for x in range(0, 10**10, 1987):
    if fnmatch(str(x), '1?6154*1'):
        print(x, x//1987)
