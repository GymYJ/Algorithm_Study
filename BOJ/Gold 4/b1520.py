import sys

sys.setrecursionlimit(100000)


def dfs(x, y, now):
    global arr, m, n, dp
    if x == m - 1 and y == n - 1:
        return 1
    if dp[x][y] != -1:
        return dp[x][y]
    dp[x][y] = 0
    move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in move:
        nx, ny = x + dx, y + dy
        if 0 <= nx < m and 0 <= ny < n and arr[nx][ny] < now:
            dp[x][y] += dfs(nx, ny, arr[nx][ny])
    return dp[x][y]


m, n = map(int, sys.stdin.readline().split())
dp = [[-1 for _ in range(n)] for _ in range(m)]
arr = []
for _ in range(m):
    arr.append(list(map(int, sys.stdin.readline().split())))
print(dfs(0, 0, arr[0][0]))
