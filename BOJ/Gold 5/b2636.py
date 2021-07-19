import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

time = 0
answer = 0
move = [[-1, 0], [1, 0], [0, -1], [0, 1]]
while True:
    visit = [[0 for _ in range(m)] for _ in range(n)]
    visit[0][0] = 1
    q = deque([[0, 0]])
    count = 0
    while q:
        x, y = q.popleft()
        for dx, dy in move:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and visit[nx][ny] == 0:
                visit[nx][ny] = 1
                if arr[nx][ny] == 0:
                    q.append([nx, ny])
                else:
                    arr[nx][ny] = 0
                    count += 1
    if count == 0:
        break
    answer = count
    time += 1
print(time)
print(answer)
