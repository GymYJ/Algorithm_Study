import sys

n = int(sys.stdin.readline())
arr = []
for i in range(n):
    age, name = sys.stdin.readline().split()
    arr.append((int(age), i, name))
arr.sort()
for age, _, name in arr:
    print(age, name)
