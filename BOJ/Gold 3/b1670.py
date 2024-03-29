import sys

n = int(sys.stdin.readline())
dp = [0 for _ in range(n + 1)]
dp[0] = 1
dp[2] = 1
for i in range(4, n + 1, 2):
    for j in range(0, i - 1, 2):
        dp[i] = (dp[i] + dp[j] * dp[i - j - 2]) % 987654321
print(dp[n])
