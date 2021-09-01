import sys
from collections import deque

h, w = map(int, sys.stdin.readline().split())
arr = []
visit = [[0 for _ in range(w)] for _ in range(h)]
q = deque([])
for i in range(h):
    temp = list(sys.stdin.readline().strip())
    for j in range(w):
        if temp[j] == '.':
            temp[j] = 0
            q.append([i, j])
        else:
            temp[j] = int(temp[j])
    arr.append(temp)
answer = 0
check = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
while q:
    x, y = q.popleft()
    for dx, dy in check:
        nx, ny = x + dx, y + dy
        if 0 <= nx < h and 0 <= ny < w and arr[nx][ny] != 0:
            arr[nx][ny] -= 1
            if arr[nx][ny] == 0:
                visit[nx][ny] = visit[x][y] + 1
                answer = max(answer, visit[nx][ny])
                q.append([nx, ny])
print(answer)
