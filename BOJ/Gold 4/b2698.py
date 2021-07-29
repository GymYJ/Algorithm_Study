import sys

t = int(sys.stdin.readline())
dp = [[[0, 0] for _ in range(101)] for _ in range(101)]
dp[1][0][0] = 1
dp[1][0][1] = 1
dp[2][0][0] = 2
dp[2][0][1] = 1
dp[2][1][1] = 1
for i in range(3, 101):
    for j in range(0, i):
        dp[i][j][0] = dp[i - 1][j][1] + dp[i - 1][j][0]
        if j == 0:
            dp[i][j][1] = dp[i - 1][j][0]
        else:
            dp[i][j][1] = dp[i - 1][j - 1][1] + dp[i - 1][j][0]

for _ in range(t):
    n, k = map(int, sys.stdin.readline().split())
    print(sum(dp[n][k]))
