import sys
from collections import deque

r, c = map(int, sys.stdin.readline().split())
arr = []
for _ in range(r):
    arr.append(list(sys.stdin.readline().strip()))
visit = [[0 for _ in range(c)] for _ in range(r)]
answer_s = 0
answer_w = 0
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for i in range(r):
    for j in range(c):
        if arr[i][j] != '#' and visit[i][j] == 0:
            sheep = 0
            wolf = 0
            q = deque([[i, j]])
            visit[i][j] = 1
            while q:
                x, y = q.popleft()
                if arr[x][y] == 'o':
                    sheep += 1
                elif arr[x][y] == 'v':
                    wolf += 1
                for dx, dy in move:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] != '#' and visit[nx][ny] == 0:
                        visit[nx][ny] = 1
                        q.append([nx, ny])
            if sheep > wolf:
                answer_s += sheep
            else:
                answer_w += wolf
print(answer_s, answer_w)
