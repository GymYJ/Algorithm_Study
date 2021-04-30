import sys
from math import inf

n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))
dp = [[inf for _ in range(3)] for _ in range(n)]
answer = inf
for i in range(3):
    for j, num in enumerate(arr[0]):
        if i == j:
            dp[0][j] = num
        else:
            dp[0][j] = inf
    for j in range(1, n - 1):
        for k in range(3):
            dp[j][k] = min([dp[j - 1][m] for m in range(3) if m != k]) + arr[j][k]
    for k in range(3):
        if k == i:
            continue
        dp[n - 1][k] = min([dp[n - 2][m] for m in range(3) if m != k]) + arr[n - 1][k]
    answer = min([answer] + dp[n - 1])
print(answer)
