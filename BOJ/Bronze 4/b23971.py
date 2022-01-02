import sys

h, w, n, m = map(int, sys.stdin.readline().split())
print(((h - 1) // (n + 1) + 1) * ((w - 1) // (m + 1) + 1))
