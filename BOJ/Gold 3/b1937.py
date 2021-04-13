import sys

sys.setrecursionlimit(100000)


def dfs(x, y, now, count):
    global n, arr, answer, visit, move, dp
    maxi = count
    for dx, dy in move:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0 and arr[nx][ny] > now:
            if dp[nx][ny] != 0:
                if maxi < dp[nx][ny] + count:
                    maxi = dp[nx][ny] + count
            else:
                visit[nx][ny] = 1
                c = dfs(nx, ny, arr[nx][ny], count + 1)
                if maxi < c + count:
                    maxi = c + count
                visit[nx][ny] = 0
    dp[x][y] = maxi - count + 1
    if answer < dp[x][y]:
        answer = dp[x][y]
    return dp[x][y]


n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))
answer = 0
visit = [[0 for _ in range(n)] for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for i in range(n):
    for j in range(n):
        if dp[i][j] == 0:
            visit[i][j] = 1
            dp[i][j] = 1
            dfs(i, j, arr[i][j], 1)
            visit[i][j] = 0
print(answer)
