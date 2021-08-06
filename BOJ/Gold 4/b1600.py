import sys
from collections import deque
from math import inf

k = int(sys.stdin.readline())
w, h = map(int, sys.stdin.readline().split())
arr = []
for _ in range(h):
    arr.append(list(map(int, sys.stdin.readline().split())))

visit = [[[inf for _ in range(k + 1)] for _ in range(w)] for _ in range(h)]
visit[0][0][0] = 0
q = deque([[0, 0, 0, 0]])
answer = -1
move = [[-1, 0], [1, 0], [0, -1], [0, 1]]
kmove = [[-1, -2], [-2, -1], [-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2]]
while q:
    x, y, knight, count = q.popleft()
    if x == h - 1 and y == w - 1:
        answer = count
        break
    if knight < k:
        for dx, dy in kmove:
            nx, ny = x + dx, y + dy
            if 0 <= nx < h and 0 <= ny < w and visit[nx][ny][knight + 1] > count + 1 and arr[nx][ny] == 0:
                visit[nx][ny][knight + 1] = count + 1
                q.append([nx, ny, knight + 1, count + 1])
    for dx, dy in move:
        nx, ny = x + dx, y + dy
        if 0 <= nx < h and 0 <= ny < w and visit[nx][ny][knight] > count + 1 and arr[nx][ny] == 0:
            visit[nx][ny][knight] = count + 1
            q.append([nx, ny, knight, count + 1])
print(answer)
