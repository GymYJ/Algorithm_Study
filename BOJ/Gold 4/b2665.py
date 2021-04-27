import sys
from collections import deque

n = int(sys.stdin.readline())
arr = [[0 for _ in range(n + 1)]]
for _ in range(n):
    arr.append([0] + list(map(int, list(sys.stdin.readline().strip()))))
visit = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
visit[1][1] = 1
move = [[-1, 0], [1, 0], [0, -1], [0, 1]]
q = deque([(1, 1, 0)])
answer = 0
while visit[n][n] == 0:
    new_q = deque([])
    while q:
        x, y, count = q.popleft()
        if x == n and y == n:
            answer = count
        for dx, dy in move:
            nx, ny = x + dx, y + dy
            if 0 < nx <= n and 0 < ny <= n and visit[nx][ny] == 0:
                if arr[nx][ny] == 1:
                    visit[nx][ny] = 1
                    q.append((nx, ny, count))
                else:
                    visit[nx][ny] = 1
                    new_q.append((nx, ny, count + 1))
    q = new_q
print(answer)
