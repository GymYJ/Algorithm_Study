import sys

n = int(sys.stdin.readline())
dp = [0 for _ in range(n + 1)]
dp[0] = 1
if n >= 2:
    dp[2] = 3
for i in range(4, n + 1):
    dp[i] = dp[i - 2] * 3
    index = i - 4
    while index >= 0:
        dp[i] += dp[index] * 2
        index -= 2
print(dp[n])
