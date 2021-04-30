import sys

n = int(sys.stdin.readline())
arr = [[]] * n
for i in range(n):
    arr[i] = list(map(int, sys.stdin.readline().split()))
arr.append(arr[0])

left = 0
right = 0
for i in range(n):
    left += arr[i][0] * arr[i + 1][1]
    right += arr[i][1] * arr[i + 1][0]
print(round(abs(left - right) / 2, 1))
