import sys

n = int(sys.stdin.readline())
arr = set()
for _ in range(n):
    temp = sys.stdin.readline().strip()
    arr.add((len(temp), temp))
arr = list(arr)
arr.sort()
for a in arr:
    print(a[1])
