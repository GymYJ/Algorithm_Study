import sys

a, b, d, n = map(int, sys.stdin.readline().split())
dp = [[0 for _ in range(3)] for _ in range(n + 1)]
dp[0][0] = 1
for i in range(1, n + 1):
    dp[i][2] = dp[i - 1][2]
    if i - d >= 0:
        dp[i][2] -= dp[i - d][0]
    if i - b >= 0:
        dp[i][2] = (dp[i][2] + dp[i - b][0]) % 1000
        dp[i - 1][1] -= dp[i - b][0]
    if i - a >= 0:
        dp[i][1] = (dp[i - a][0] + dp[i - 1][1]) % 1000
        dp[i][0] = dp[i][1]
answer = sum(dp[n])
for i in range(n - 1, n - a, -1):
    answer += dp[i][0]
print(answer % 1000)
