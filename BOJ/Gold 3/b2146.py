import sys
from collections import deque

n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))
visit = [[0 for _ in range(n)] for _ in range(n)]
count = 1
move = [[-1, 0], [1, 0], [0, -1], [0, 1]]
edge = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and visit[i][j] == 0:
            visit[i][j] = count
            q = deque([(i, j)])
            while q:
                x, y = q.popleft()
                is_edge = False
                for dx, dy in move:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n:
                        if arr[nx][ny] == 1 and visit[nx][ny] == 0:
                            visit[nx][ny] = count
                            q.append((nx, ny))
                        elif arr[nx][ny] == 0:
                            is_edge = True
                if is_edge:
                    edge.append((x, y))
            count += 1
arr = visit
answer = 10000
for i, j in edge:
    visit = [[0 for _ in range(n)] for _ in range(n)]
    q = deque([(i, j, arr[i][j], 0)])
    while q:
        x, y, island, leng = q.popleft()
        if answer < leng:
            continue
        for dx, dy in move:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] == 0 and visit[nx][ny] == 0:
                    visit[nx][ny] = 1
                    q.append((nx, ny, island, leng + 1))
                elif arr[nx][ny] != 0 and arr[nx][ny] != island:
                    if answer > leng:
                        answer = leng
print(answer)
