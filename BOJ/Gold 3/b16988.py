import sys
from collections import deque


def bfs(picks):
    global n, m, arr, answer
    for i, j in picks:
        arr[i][j] = 1
    visit = [[0 for _ in range(m)] for _ in range(n)]
    move = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    total = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 2 and visit[i][j] == 0:
                visit[i][j] = 1
                q = deque([[i, j]])
                count = 1
                is_p = True
                while q:
                    x, y = q.popleft()
                    for dx, dy in move:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < m and visit[nx][ny] == 0:
                            if arr[nx][ny] == 2:
                                visit[nx][ny] = 1
                                q.append([nx, ny])
                                count += 1
                            elif arr[nx][ny] == 0:
                                is_p = False
                if is_p:
                    total += count
    answer = max(answer, total)
    for i, j in picks:
        arr[i][j] = 0


def dfs(x, y, now):
    global n, m, arr
    if y == m:
        x += 1
        y = 0
    if len(now) == 2:
        bfs(now)
        return
    while x < n:
        while y < m:
            if arr[x][y] == 0:
                dfs(x, y + 1, now + [[x, y]])
            y += 1
            if y == m:
                break
        y = 0
        x += 1


sys.setrecursionlimit(100000)
n, m = map(int, sys.stdin.readline().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))
answer = 0
dfs(0, 0, [])
print(answer)
