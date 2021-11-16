import sys

t = int(sys.stdin.readline())
dp = [[0 for _ in range(65)] for _ in range(10)]
for i in range(10):
    dp[i][1] = i + 1
for i in range(2, 65):
    for j in range(10):
        if j == 0:
            dp[j][i] = 1
        else:
            dp[j][i] = dp[j - 1][i] + dp[j][i - 1]
for _ in range(t):
    n = int(sys.stdin.readline())
    print(dp[9][n])
