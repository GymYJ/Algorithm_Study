import sys

n = int(sys.stdin.readline())
arr = [[0 for _ in range(n + 1)]]
for _ in range(n):
    arr.append([0] + list(map(int, sys.stdin.readline().split())))
dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
dp[1][1] = 1
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == n and j == n:
            break
        if i + arr[i][j] <= n:
            dp[i + arr[i][j]][j] += dp[i][j]
        if j + arr[i][j] <= n:
            dp[i][j + arr[i][j]] += dp[i][j]
print(dp[n][n])
