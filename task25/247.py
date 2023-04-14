from fnmatch import fnmatch

n = 700001
k = 0
while k < 5:
    if n % 13 == 0 and not fnmatch(str(n), '*0??3*') and not fnmatch(str(n), '*4??2') and not fnmatch(str(n), '*1*'):
        print(n, sum(map(int, str(n))))
        k += 1
    n += 1