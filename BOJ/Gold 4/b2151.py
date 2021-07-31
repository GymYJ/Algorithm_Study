import sys
from collections import deque
from math import inf

n = int(sys.stdin.readline())
arr = []
door = []
for i in range(n):
    temp = list(sys.stdin.readline().strip())
    arr.append(temp)
    for j in range(n):
        if temp[j] == '#':
            door.append([i, j])
visit = [[[[inf for _ in range(3)] for _ in range(3)] for _ in range(n)] for _ in range(n)]
move = [[-1, 0], [1, 0], [0, -1], [0, 1]]
start = []
for m in move:
    start.append(door[0] + m + [0])
answer = sys.maxsize
q = deque(start)
while q:
    x, y, mx, my, c = q.popleft()
    if c > answer:
        continue
    if [x, y] == door[1]:
        answer = min(answer, c)
    if arr[x][y] == '!':
        if mx == 0:
            move = [[my, mx], [-my, mx]]
        else:
            move = [[my, mx], [my, -mx]]
        for dx, dy in move:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] != '*' and visit[nx][ny][dx][dy] > c + 1:
                visit[nx][ny][dx][dy] = c + 1
                q.append([nx, ny, dx, dy, c + 1])
    nx, ny = x + mx, y + my
    if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] != '*' and visit[nx][ny][mx][my] > c:
        visit[nx][ny][mx][my] = c
        q.append([nx, ny, mx, my, c])
print(answer)
