import sys
from collections import deque
from itertools import combinations

S = []
Y = []
for i in range(5):
    temp = list(sys.stdin.readline().strip())
    for j in range(5):
        if temp[j] == 'S':
            S.append((i, j))
        else:
            Y.append((i, j))
answer = 0
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
if len(S) <= 7:
    size = len(S) + 1
else:
    size = 8
for n in range(4, size):
    for ss in combinations(S, n):
        if n != 7:
            for yy in combinations(Y, 7 - n):
                arr = [[0 for _ in range(5)] for _ in range(5)]
                visit = [[0 for _ in range(5)] for _ in range(5)]
                for i, j in ss:
                    arr[i][j] = 1
                for i, j in yy:
                    arr[i][j] = 1
                i, j = ss[0]
                q = deque([(i, j)])
                visit[i][j] = 1
                count = 1
                while q:
                    x, y = q.popleft()
                    for dx, dy in move:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < 5 and 0 <= ny < 5 and visit[nx][ny] == 0 and arr[nx][ny] == 1:
                            q.append((nx, ny))
                            visit[nx][ny] = 1
                            count += 1
                if count == 7:
                    answer += 1
        else:
            arr = [[0 for _ in range(5)] for _ in range(5)]
            visit = [[0 for _ in range(5)] for _ in range(5)]
            for i, j in ss:
                arr[i][j] = 1
            i, j = ss[0]
            q = deque([(i, j)])
            visit[i][j] = 1
            count = 1
            while q:
                x, y = q.popleft()
                for dx, dy in move:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < 5 and 0 <= ny < 5 and visit[nx][ny] == 0 and arr[nx][ny] == 1:
                        q.append((nx, ny))
                        visit[nx][ny] = 1
                        count += 1
            if count == 7:
                answer += 1
print(answer)
