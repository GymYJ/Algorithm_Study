import sys
import copy
from collections import deque

n, m = map(int, sys.stdin.readline().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))
year = 0
change = True
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
while change:
    change = False
    visit = [[0 for _ in range(m)] for _ in range(n)]
    count = 0
    new_arr = copy.deepcopy(arr)
    for i in range(n):
        for j in range(m):
            if arr[i][j] > 0 and visit[i][j] == 0:
                count += 1
                visit[i][j] = 1
                q = deque([(i, j)])
                while q:
                    x, y = q.popleft()
                    for dx, dy in move:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < m:
                            if arr[nx][ny] == 0 and new_arr[x][y] > 0:
                                new_arr[x][y] -= 1
                            elif arr[nx][ny] > 0 and visit[nx][ny] == 0:
                                q.append((nx, ny))
                                visit[nx][ny] = 1
                change = True
    arr = new_arr
    if not change:
        print(0)
        break
    if count > 1:
        print(year)
        break
    year += 1
