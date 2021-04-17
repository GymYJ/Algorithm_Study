import sys

n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    arr.append((a, b))
arr.sort()
for a, b in arr:
    print(a, b)
