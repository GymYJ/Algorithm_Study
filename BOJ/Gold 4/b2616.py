import sys

n = int(sys.stdin.readline())
arr = [0] + list(map(int, sys.stdin.readline().split()))
k = int(sys.stdin.readline())
accu = [0 for _ in range(n + 1)]
for i in range(1, n + 1):
    accu[i] = accu[i - 1] + arr[i]
dp = [[0 for _ in range(n + 1)] for _ in range(3)]
for i in range(3):
    for j in range((i + 1) * k, n + 1):
        if i == 0:
            dp[i][j] = max(dp[i][j - 1], accu[j] - accu[j - k])
        else:
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j - k] + accu[j] - accu[j - k])
print(dp[-1][-1])
