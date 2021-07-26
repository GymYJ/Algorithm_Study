import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))
visit = [[0 for _ in range(m)] for _ in range(n)]
move = [[-1, 0], [1, 0], [0, -1], [0, 1]]
count = 0
biggest = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and visit[i][j] == 0:
            visit[i][j] = 1
            count += 1
            q = deque([[i, j]])
            size = 1
            while q:
                x, y = q.popleft()
                for dx, dy in move:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 1 and visit[nx][ny] == 0:
                        visit[nx][ny] = 1
                        size += 1
                        q.append([nx, ny])
            if biggest < size:
                biggest = size
print(count)
print(biggest)
