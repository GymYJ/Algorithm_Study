import sys
import re

t = int(sys.stdin.readline())
q = re.compile('^((10)0+1+|01)+$')
for _ in range(t):
    data = sys.stdin.readline().strip()
    if q.match(data):
        print('YES')
    else:
        print('NO')
