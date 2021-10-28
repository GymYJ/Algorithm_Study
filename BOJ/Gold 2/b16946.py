import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, list(sys.stdin.readline().strip()))))
answer = []
visit = [[0 for _ in range(m)] for _ in range(n)]
counter = [[[None, 0] for _ in range(m)] for _ in range(n)]
move = [[-1, 0], [1, 0], [0, -1], [0, 1]]
numbering = 1
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0 and visit[i][j] == 0:
            visit[i][j] = 1
            temp = [(i, j)]
            q = deque([[i, j]])
            while q:
                x, y = q.popleft()
                for dx, dy in move:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0 and visit[nx][ny] == 0:
                        visit[nx][ny] = 1
                        temp.append((nx, ny))
                        q.append([nx, ny])
            size = len(temp)
            for x, y in temp:
                counter[x][y] = [numbering, size]
            numbering += 1
for i in range(n):
    temp = []
    for j in range(m):
        if arr[i][j] == 0:
            temp.append(0)
        else:
            count = 1
            check = []
            for dx, dy in move:
                nx, ny = i + dx, j + dy
                if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0 and not counter[nx][ny][0] in check:
                    check.append(counter[nx][ny][0])
                    count += counter[nx][ny][1]
            temp.append(count % 10)
    answer.append(temp)
for row in answer:
    print(''.join(map(str, row)))
