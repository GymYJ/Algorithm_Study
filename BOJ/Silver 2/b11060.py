import sys
from math import inf

sys.setrecursionlimit(1000000)


def dfs(now):
    global n, arr, dp
    if now >= n - 1:
        return 0
    if dp[now] != inf:
        return dp[now]
    if arr[now] == 0:
        return dp[now]
    dp[now] = min([dfs(now + i) for i in range(1, arr[now] + 1)]) + 1
    return dp[now]


n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
dp = [inf] * n
dp[-1] = 0
dfs(0)
print(dp[0] if dp[0] != inf else -1)
