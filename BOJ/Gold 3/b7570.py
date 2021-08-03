import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
dp = [0 for _ in range(n + 1)]
long = 0
for i in range(n):
    idx = arr[i]
    dp[idx] = dp[idx - 1] + 1
    long = max(long, dp[idx])
print(n - max(dp))
