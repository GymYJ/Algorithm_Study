import sys

n, m, k = map(int, sys.stdin.readline().split())
dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
dp[1][1] = 1
if k != 0:
    if k % m == 0:
        x = k // m
        y = m
    else:
        x = k // m + 1
        y = k % m
    for i in range(1, x + 1):
        for j in range(1, y + 1):
            if i == 1 and j == 1:
                continue
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    for i in range(x, n + 1):
        for j in range(y, m + 1):
            if i == x and j == y:
                continue
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    print(dp[n][m])
else:
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                continue
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    print(dp[n][m])
