import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))
move = [(-1, 0), (0, 1), (1, 0), (0, -1)]
now = d
q = deque([(r, c)])
arr[r][c] = -1
clean = 1
while q:
    x, y = q.popleft()
    find = False
    for _ in range(4):
        if now == 0:
            now = 3
        else:
            now -= 1
        n_x, n_y = x + move[now][0], y + move[now][1]
        if arr[n_x][n_y] == 0:
            q.append((n_x, n_y))
            arr[n_x][n_y] = -1
            clean += 1
            find = True
            break
        elif arr[n_x][n_y] == -1:
            continue
    if not find:
        n_x, n_y = x + (move[now][0] * -1), y + (move[now][1] * -1)
        if arr[n_x][n_y] == -1:
            q.append((n_x, n_y))
        elif arr[n_x][n_y] == 1:
            break
print(clean)
