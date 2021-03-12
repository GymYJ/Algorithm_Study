import sys

n, k = map(int, sys.stdin.readline().split())
coin = []
for _ in range(n):
    num = int(sys.stdin.readline())
    if num <= k:
        coin.append(num)
coin.sort()
dp = [0 for _ in range(k + 1)]
now = coin[0]
while now <= k:
    dp[now] += 1
    now += coin[0]
for c in coin[1:]:
    now = c
    dp[now] += 1
    for i in range(now, k + 1):
        if i - now > 0 and dp[i - now] >= 0:
            dp[i] += dp[i - now]
print(dp[k])
