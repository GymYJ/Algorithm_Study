import sys


def dfs(a, b, c):
    global dp
    if a < 0:
        a = 0
    if b < 0:
        b = 0
    if c < 0:
        c = 0
    if a == 0 and b == 0 and c == 0:
        return 0
    if dp[a][b][c] != 0:
        return dp[a][b][c]
    dp[a][b][c] = min(dfs(a - 9, b - 3, c - 1) + 1, dfs(a - 9, b - 1, c - 3) + 1,
                      dfs(a - 3, b - 9, c - 1) + 1, dfs(a - 1, b - 9, c - 3) + 1,
                      dfs(a - 3, b - 1, c - 9) + 1, dfs(a - 1, b - 3, c - 9) + 1,
                      )
    return dp[a][b][c]


n = int(sys.stdin.readline())
scv = list(map(int, sys.stdin.readline().split()))
for i in range(n, 3):
    scv.append(0)
dp = [[[0 for _ in range(61)] for _ in range(61)] for _ in range(61)]
dfs(scv[0], scv[1], scv[2])
print(dp[scv[0]][scv[1]][scv[2]])
