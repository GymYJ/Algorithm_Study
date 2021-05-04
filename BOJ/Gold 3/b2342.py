import sys
from math import inf

sys.setrecursionlimit(1000000)


def move(now, target):
    if now == 0:
        return 2
    elif now == target:
        return 1
    elif abs(now - target) == 2:
        return 4
    else:
        return 3


def dfs(power, idx, foot):
    global arr, n, dp
    if idx == n:
        return 0
    if dp[idx][foot[0]][foot[1]] != inf:
        return dp[idx][foot[0]][foot[1]]
    dp[idx][foot[0]][foot[1]] = min(dfs(power, idx + 1, [arr[idx], foot[1]]) + move(foot[0], arr[idx]),
                                    dfs(power, idx + 1, [foot[0], arr[idx]]) + move(foot[1], arr[idx]))
    return dp[idx][foot[0]][foot[1]]


arr = list(map(int, sys.stdin.readline().split()))[:-1]
n = len(arr)
if n == 0:
    print(0)
    sys.exit()
dp = [[[inf for _ in range(5)] for _ in range(5)] for _ in range(n)]
dfs(0, 0, [0, 0])
print(dp[0][0][0])
