import sys

t = int(sys.stdin.readline())
for _ in range(t):
    h, w, n = map(int, sys.stdin.readline().split())
    x = n // h if n % h == 0 else n // h + 1
    y = h if n % h == 0 else n % h
    print('%d%02d' % (y, x))
