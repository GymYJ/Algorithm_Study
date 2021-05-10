import sys

sys.setrecursionlimit(100000)


def dfs(turn, left, right):
    global arr, dp
    if left > right:
        return 0
    if dp[left][right] != 0:
        return dp[left][right]

    if turn:
        score = max(dfs(False, left + 1, right) + arr[left], dfs(False, left, right - 1) + arr[right])
    else:
        score = min(dfs(True, left + 1, right), dfs(True, left, right - 1))
    dp[left][right] = score
    return score


t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    dp = [[0 for _ in range(n)] for _ in range(n)]
    dfs(True, 0, n - 1)
    print(dp[0][n - 1])
