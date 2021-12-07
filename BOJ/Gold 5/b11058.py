import sys

n = int(sys.stdin.readline())
dp = [0 for _ in range(101)]
for i in range(1, 7):
    dp[i] = i
for i in range(7, n + 1):
    dp[i] = dp[i - 1] + 1
    for j in range(3, i):
        dp[i] = max(dp[i], dp[i - j] * (j - 1))
print(dp[n])
