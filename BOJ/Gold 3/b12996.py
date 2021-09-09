import sys

s, do, ke, ho = map(int, sys.stdin.readline().split())
dp = [[[[0 for _ in range(ho + 1)] for _ in range(ke + 1)] for _ in range(do + 1)] for _ in range(s + 1)]
dp[0][0][0][0] = 1
for i in range(1, s + 1):
    for d in range(do + 1):
        for k in range(ke + 1):
            for h in range(ho + 1):
                if d == 0 and k == 0 and h == 0:
                    continue
                if d != 0:
                    dp[i][d][k][h] = (dp[i][d][k][h] + dp[i - 1][d - 1][k][h]) % 1000000007
                if k != 0:
                    dp[i][d][k][h] = (dp[i][d][k][h] + dp[i - 1][d][k - 1][h]) % 1000000007
                if h != 0:
                    dp[i][d][k][h] = (dp[i][d][k][h] + dp[i - 1][d][k][h - 1]) % 1000000007
                if d != 0 and k != 0:
                    dp[i][d][k][h] = (dp[i][d][k][h] + dp[i - 1][d - 1][k - 1][h]) % 1000000007
                if d != 0 and h != 0:
                    dp[i][d][k][h] = (dp[i][d][k][h] + dp[i - 1][d - 1][k][h - 1]) % 1000000007
                if k != 0 and h != 0:
                    dp[i][d][k][h] = (dp[i][d][k][h] + dp[i - 1][d][k - 1][h - 1]) % 1000000007
                if d != 0 and k != 0 and h != 0:
                    dp[i][d][k][h] = (dp[i][d][k][h] + dp[i - 1][d - 1][k - 1][h - 1]) % 1000000007

print(dp[s][do][ke][ho])
