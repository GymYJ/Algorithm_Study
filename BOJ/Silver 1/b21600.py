import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
dp = [1] * n
for i in range(1, n):
    if arr[i] > dp[i - 1]:
        dp[i] = dp[i - 1] + 1
    else:
        dp[i] = arr[i]
print(max(dp))
