import sys

t = int(sys.stdin.readline())
dp = [0 for _ in range(5001)]
dp[0] = 1
dp[2] = 1
dp[4] = 2
for i in range(6, 5001, 2):
    for j in range(2, i + 1, 2):
        dp[i] = (dp[i] + dp[j - 2] * dp[i - j]) % 1000000007
for _ in range(t):
    L = int(sys.stdin.readline())
    print(dp[L])
