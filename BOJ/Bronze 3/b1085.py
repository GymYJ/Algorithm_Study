import sys

x, y, w, h = map(int, sys.stdin.readline().split())
print(min(min(x, w - x), min(y, h - y)))
