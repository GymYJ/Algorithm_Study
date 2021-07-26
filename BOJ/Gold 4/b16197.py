import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
arr = []
coin = []
for i in range(n):
    temp = list(sys.stdin.readline().strip())
    for j in range(m):
        if temp[j] == 'o':
            coin.append([i, j])
    arr.append(temp)
visit = [[[[0 for _ in range(m)] for _ in range(n)] for _ in range(m)] for _ in range(n)]
visit[coin[0][0]][coin[0][1]][coin[1][0]][coin[1][1]] = 1
q = deque([[coin[0][0], coin[0][1], coin[1][0], coin[1][1], 0]])
move = [[-1, 0], [1, 0], [0, -1], [0, 1]]
answer = -1
while q:
    x1, y1, x2, y2, c = q.popleft()
    if c >= 10:
        continue
    for dx, dy in move:
        nx1, ny1, nx2, ny2 = x1 + dx, y1 + dy, x2 + dx, y2 + dy
        out = 0
        if nx1 < 0 or nx1 >= n or ny1 < 0 or ny1 >= m:
            out += 1
        if nx2 < 0 or nx2 >= n or ny2 < 0 or ny2 >= m:
            out += 1
        if out == 1:
            answer = c + 1
            break
        elif out == 2:
            continue
        else:
            if arr[nx1][ny1] == '#':
                nx1, ny1 = x1, y1
            if arr[nx2][ny2] == '#':
                nx2, ny2 = x2, y2
            if visit[nx1][ny1][nx2][ny2] == 0:
                visit[nx1][ny1][nx2][ny2] = 1
                q.append([nx1, ny1, nx2, ny2, c + 1])
    if answer != -1:
        break
print(answer)
