import sys
from math import sqrt

n = int(sys.stdin.readline())
dp = [5 for _ in range(n + 1)]
for i in range(1, int(sqrt(n)) + 1):
    num = i ** 2
    dp[num] = 1
    for j in range(num + 1, num * 4 + 1):
        if j > n:
            break
        dp[j] = min(dp[j], dp[j - num] + 1)
print(dp[n])
