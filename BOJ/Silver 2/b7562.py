import sys
from collections import deque

t = int(sys.stdin.readline())
move = [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2)]
for _ in range(t):
    l = int(sys.stdin.readline())
    visit = [[0 for _ in range(l)] for _ in range(l)]
    now = list(map(int, sys.stdin.readline().split()))
    target = list(map(int, sys.stdin.readline().split()))
    visit[now[0]][now[1]] = 1
    q = deque([now + [0]])
    while q:
        x, y, c = q.popleft()
        if x == target[0] and y == target[1]:
            print(c)
            break
        for dx, dy in move:
            nx, ny = x + dx, y + dy
            if 0 <= nx < l and 0 <= ny < l and visit[nx][ny] == 0:
                q.append([nx, ny, c + 1])
                visit[nx][ny] = 1
