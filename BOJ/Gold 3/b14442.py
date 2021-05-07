import sys
from collections import deque

n, m, k = map(int, sys.stdin.readline().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, list(sys.stdin.readline().strip()))))
crushed = [[-1 for _ in range(m)] for _ in range(n)]
crushed[0][0] = k
route = [[0 for _ in range(m)] for _ in range(n)]
route[0][0] = 1
q = deque([(0, 0, 1, k)])
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
answer = 10000000
while q:
    x, y, length, crush = q.popleft()
    if x == n - 1 and y == m - 1:
        if answer > length:
            answer = length
        continue
    for dx, dy in move:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m:
            if arr[nx][ny] == 0:
                if crushed[nx][ny] < crush:
                    q.append((nx, ny, length + 1, crush))
                    crushed[nx][ny] = crush
            else:
                if crush > 0 and crushed[nx][ny] < crush - 1:
                    q.append((nx, ny, length + 1, crush - 1))
                    crushed[nx][ny] = crush - 1
print(answer if answer != 10000000 else -1)
