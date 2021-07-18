import sys
from math import inf

n, k = map(int, sys.stdin.readline().split())
coin = set()
for _ in range(n):
    coin.add(int(sys.stdin.readline()))
coin = sorted(list(coin))
dp = [inf for _ in range(100001)]
dp[0] = 0
for c in coin:
    for i in range(c, 100001):
        dp[i] = min(dp[i], dp[i - c] + 1)
print(dp[k] if dp[k] != inf else -1)
