import sys

n = int(sys.stdin.readline())
dp = [-1 for _ in range(5001)]
dp[3] = 1
dp[5] = 1
for i in range(6, 5001):
    temp = []
    if dp[i - 3] > 0:
        temp.append(dp[i - 3])
    if dp[i - 5] > 0:
        temp.append(dp[i - 5])
    if temp:
        dp[i] = min(temp) + 1
print(dp[n])
