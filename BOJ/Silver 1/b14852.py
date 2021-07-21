import sys

n = int(sys.stdin.readline())
dp = [1 for _ in range(n + 3)]
dp2 = [0 for _ in range(n + 3)]
dp[1] = 2
dp[2] = 7
dp2[3] = 1
for i in range(3, n + 1):
    dp[i] = ((dp[i - 1] * 2) + (dp[i - 2] * 3) + (dp2[i] * 2)) % 1000000007
    dp2[i + 1] = (dp2[i] + dp[i - 2]) % 1000000007
print(dp[n])