import sys
from collections import deque
from math import inf
from itertools import permutations

arr = []
for _ in range(5):
    temp = []
    for _ in range(5):
        temp.append(list(map(int, sys.stdin.readline().split())))
    arr.append(temp)
answer = inf
copy_arr = arr.copy()
move = [[-1, 0, 0], [1, 0, 0], [0, -1, 0], [0, 1, 0], [0, 0, -1], [0, 0, 1]]
for a in range(4):
    if a > 0:
        temp = [[0 for _ in range(5)] for _ in range(5)]
        for i in range(5):
            for j in range(5):
                temp[i][j] = arr[0][4 - j][i]
        arr[0] = temp.copy()
    for b in range(4):
        if b > 0:
            temp = [[0 for _ in range(5)] for _ in range(5)]
            for i in range(5):
                for j in range(5):
                    temp[i][j] = arr[1][4 - j][i]
            arr[1] = temp.copy()
        for c in range(4):
            if c > 0:
                temp = [[0 for _ in range(5)] for _ in range(5)]
                for i in range(5):
                    for j in range(5):
                        temp[i][j] = arr[2][4 - j][i]
                arr[2] = temp.copy()
            for d in range(4):
                if d > 0:
                    temp = [[0 for _ in range(5)] for _ in range(5)]
                    for i in range(5):
                        for j in range(5):
                            temp[i][j] = arr[3][4 - j][i]
                    arr[3] = temp.copy()
                for e in range(4):
                    if e > 0:
                        temp = [[0 for _ in range(5)] for _ in range(5)]
                        for i in range(5):
                            for j in range(5):
                                temp[i][j] = arr[4][4 - j][i]
                        arr[4] = temp.copy()
                    for p in permutations([0, 1, 2, 3, 4]):
                        new_arr = [arr[p[0]], arr[p[1]], arr[p[2]], arr[p[3]], arr[p[4]]]
                        if new_arr[0][0][0] == 1:
                            visit = [[[0 for _ in range(5)] for _ in range(5)] for _ in range(5)]
                            visit[0][0][0] = 1
                            q = deque([[0, 0, 0, 0]])
                            while q:
                                x, y, z, count = q.popleft()
                                if x == 4 and y == 4 and z == 4:
                                    answer = min(answer, count)
                                    continue
                                for dx, dy, dz in move:
                                    nx, ny, nz = x + dx, y + dy, z + dz
                                    if 0 <= nx < 5 and 0 <= ny < 5 and 0 <= nz < 5 and visit[nx][ny][nz] == 0 and \
                                            new_arr[nx][ny][nz] == 1:
                                        visit[nx][ny][nz] = 1
                                        q.append([nx, ny, nz, count + 1])
                arr[4] = copy_arr[4].copy()
            arr[3] = copy_arr[3].copy()
        arr[2] = copy_arr[2].copy()
    arr[1] = copy_arr[1].copy()
print(answer if answer != inf else -1)
