import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
switch = [[[] for _ in range(n + 1)] for _ in range(n + 1)]
for _ in range(m):
    x, y, a, b = map(int, sys.stdin.readline().split())
    switch[x][y].append([a, b])
light = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
visit = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
light[1][1] = 1
visit[1][1] = 1
q = deque([[1, 1]])
move = [[-1, 0], [1, 0], [0, -1], [0, 1]]
while q:
    x, y = q.popleft()
    for a, b in switch[x][y]:
        if light[a][b] == 0:
            light[a][b] = 1
            for dx, dy in move:
                nx, ny = a + dx, b + dy
                if 0 < nx <= n and 0 < ny <= n and visit[nx][ny] == 1:
                    q.append([a, b])
                    visit[a][b] = 1
                    break
    for dx, dy in move:
        nx, ny = x + dx, y + dy
        if 0 < nx <= n and 0 < ny <= n and visit[nx][ny] == 0 and light[nx][ny] == 1:
            q.append([nx, ny])
            visit[nx][ny] = 1
print(sum(map(sum, light)))
