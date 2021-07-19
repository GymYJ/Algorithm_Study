import sys

n = int(sys.stdin.readline())
arr = [0] + list(map(int, sys.stdin.readline().split()))
dp = [[0 for _ in range(21)] for _ in range(n + 1)]
dp[1][arr[1]] = 1
for i in range(2, n):
    num = arr[i]
    for j in range(0, 21):
        if j + num <= 20:
            dp[i][j + num] += dp[i - 1][j]
        if j - num >= 0:
            dp[i][j - num] += dp[i - 1][j]
print(dp[n - 1][arr[-1]])
