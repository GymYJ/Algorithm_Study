import sys

n, k = map(int, sys.stdin.readline().split())
coin = []
for _ in range(n):
    num = int(sys.stdin.readline())
    if num <= k:
        coin.append(num)
coin.sort()
dp = {i: dict() for i in range(1, k+1)}
for i in range(1, k + 1):
    for j, c in enumerate(coin):
        if c == i:
            dp[i][c] = 1
        if c < i:
            dp[i][c] = sum(dp[i - c].values())
            if c in dp[i - c]:
                del dp[i - c][c]
                temp = i - c
    if i - coin[-1] > 0:
        del dp[i - coin[-1]]
print(sum(dp[k].values()))
