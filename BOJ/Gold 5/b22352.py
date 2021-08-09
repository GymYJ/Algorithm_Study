import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
before = []
after = []
for _ in range(n):
    before.append(list(map(int, sys.stdin.readline().split())))
for _ in range(n):
    after.append(list(map(int, sys.stdin.readline().split())))
visit = [[0 for _ in range(m)] for _ in range(n)]
change = 0
move = [[-1, 0], [1, 0], [0, -1], [0, 1]]
for i in range(n):
    for j in range(m):
        if visit[i][j] == 0:
            visit[i][j] = 1
            q = deque([[i, j]])
            be, af = before[i][j], after[i][j]
            if be != af:
                change += 1
            while q:
                x, y = q.popleft()
                for dx, dy in move:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < m and visit[nx][ny] == 0 and before[nx][ny] == be:
                        if after[nx][ny] == af:
                            visit[nx][ny] = 1
                            q.append([nx, ny])
                        else:
                            print('NO')
                            sys.exit()
if change > 1:
    print('NO')
else:
    print('YES')
