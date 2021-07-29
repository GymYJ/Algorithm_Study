import sys


def dfs(now, before, color):
    global board, visit, n, m
    if visit[now[0]][now[1]] == 1:
        return True
    visit[now[0]][now[1]] = 1
    move = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    for dx, dy in move:
        nx, ny = now[0] + dx, now[1] + dy
        if 0 <= nx < n and 0 <= ny < m and (before[0] != nx or before[1] != ny) and board[nx][ny] == color:
            if dfs([nx, ny], now, color):
                return True
    return False


n, m = map(int, sys.stdin.readline().split())
board = []
for _ in range(n):
    board.append(list(sys.stdin.readline().strip()))
visit = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if visit[i][j] == 0:
            if dfs([i, j], [-1, -1], board[i][j]):
                print('Yes')
                sys.exit()
print('No')
