import sys

n, m = map(int, sys.stdin.readline().split())
arr = [[0 for _ in range(m + 1)]]
for _ in range(n):
    arr.append([0] + list(map(int, sys.stdin.readline().split())))
dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
for x in range(1, n + 1):
    for y in range(1, m + 1):
        dp[x][y] = max(dp[x - 1][y - 1], dp[x - 1][y], dp[x][y - 1]) + arr[x][y]
print(dp[n][m])
