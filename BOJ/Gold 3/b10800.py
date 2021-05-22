import sys
from collections import defaultdict

n = int(sys.stdin.readline())
arr = []
for i in range(n):
    c, s = map(int, sys.stdin.readline().split())
    arr.append((s, c, i))
arr.sort()

answer = defaultdict(int)
color_sum = defaultdict(int)
total = 0
j = 0
for i in range(n):
    while arr[j][0] < arr[i][0]:
        total += arr[j][0]
        color_sum[arr[j][1]] += arr[j][0]
        j += 1
    answer[arr[i][2]] = total - color_sum[arr[i][1]]
for i in range(n):
    print(answer[i])
