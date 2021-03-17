import sys

n, k = map(int, sys.stdin.readline().split())
dp = [1 for _ in range(n + 1)]
for i in range(1, n + 1):
    dp[i] = dp[i - 1] * i
print(dp[n] // (dp[k] * dp[n - k]) % 10007)
