import sys

t = int(sys.stdin.readline())
k = int(sys.stdin.readline())
coins = []
for _ in range(k):
    coins.append(list(map(int, sys.stdin.readline().split())))
coins.sort()
dp = [[0 for _ in range(t + 1)] for _ in range(k)]
p, n = coins[0]
for i in range(p, min(p * n, t) + 1, p):
    dp[0][i] = 1
for i in range(1, k):
    p, n = coins[i]
    for j in range(1, t + 1):
        dp[i][j] += dp[i - 1][j]
    for j in range(p, min(p * n, t) + 1, p):
        dp[i][j] += 1
        for k in range(j + 1, t + 1):
            dp[i][k] += dp[i - 1][k - j]
print(dp[-1][t])
