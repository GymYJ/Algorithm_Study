import sys

n = int(sys.stdin.readline())
arr = [0] * 10001
for _ in range(n):
    arr[int(sys.stdin.readline())] += 1
for i, num in enumerate(arr):
    while num > 0:
        print(i)
        num -= 1
