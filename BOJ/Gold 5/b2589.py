import sys
from collections import deque

s, g = map(int, sys.stdin.readline().split())
arr = []
for _ in range(s):
    arr.append(list(sys.stdin.readline().strip()))
answer = 0
move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
for i in range(s):
    for j in range(g):
        if arr[i][j] == 'L':
            q = deque([(i, j, 0)])
            visit = [[0 for _ in range(g)] for _ in range(s)]
            visit[i][j] = 1
            while q:
                x, y, count = q.popleft()
                if answer < count:
                    answer = count
                for dx, dy in move:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < s and 0 <= ny < g and visit[nx][ny] == 0 and arr[nx][ny] == 'L':
                        q.append((nx, ny, count + 1))
                        visit[nx][ny] = 1
print(answer)
