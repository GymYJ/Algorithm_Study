import sys
from math import inf


def dfs(now, visit):
    global n, arr, dp
    if visit == 2 ** n - 1:
        if arr[now][0]:
            return arr[now][0]
        else:
            return inf
    if dp[now][visit] != inf:
        return dp[now][visit]
    for i in range(1, n):
        if not arr[now][i]:
            continue
        if visit & (2 ** i):
            continue
        dp[now][visit] = min(dp[now][visit], dfs(i, visit | (2 ** i)) + arr[now][i])
    return dp[now][visit]


n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))
dp = [[inf for _ in range(2 ** n)] for _ in range(n)]
dfs(0, 1)
print(dp[0][1])
