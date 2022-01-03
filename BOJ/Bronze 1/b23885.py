import sys

n, m = map(int, sys.stdin.readline().split())
sx, sy = map(int, sys.stdin.readline().split())
ex, ey = map(int, sys.stdin.readline().split())
if sx == ex and sy == ey:
    print('YES')
    sys.exit()
if n == 1 or m == 1:
    print('NO')
    sys.exit()
if (sx + sy) % 2 == 0:
    if (ex + ey) % 2 == 0:
        print('YES')
    else:
        print('NO')
else:
    if (ex + ey) % 2 == 1:
        print('YES')
    else:
        print('NO')
