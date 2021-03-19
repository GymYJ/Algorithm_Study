import sys
from collections import deque

n, l, r = map(int, sys.stdin.readline().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))
answer = 0
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
change = True
while change:
    change = False
    visit = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if visit[i][j] == 0:
                visit[i][j] = 1
                union = [(i, j)]
                q = deque([(i, j)])
                while q:
                    x, y = q.popleft()
                    for dx, dy in move:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0 and \
                                l <= abs(arr[x][y] - arr[nx][ny]) <= r:
                            visit[nx][ny] = 1
                            union.append((nx, ny))
                            q.append((nx, ny))
                if len(union) > 1:
                    change = True
                    value = sum(arr[x][y] for x, y in union) // len(union)
                    for x, y in union:
                        arr[x][y] = value
    if not change:
        break
    answer += 1

print(answer)
