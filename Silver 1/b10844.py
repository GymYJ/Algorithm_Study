import sys

n = int(sys.stdin.readline())
dp = [1 for _ in range(10)]
dp[0] = 0
for i in range(2, n + 1):
    new_dp = [0 for _ in range(10)]
    new_dp[0] = dp[1]
    new_dp[1] = dp[0] + dp[2] if dp[0] != 0 else dp[2]
    for n in range(2, 9):
        new_dp[n] = dp[n - 1] + dp[n + 1]
    new_dp[9] = dp[8]
    dp = new_dp
print(sum(dp) % 1000000000)
