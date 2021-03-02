import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))
for i in range(m):
    arr[0][i] = 2
    arr[n - 1][i] = 2
for i in range(n):
    arr[i][0] = 2
    arr[i][m - 1] = 2

x_list = [-1, 1, 0, 0]
y_list = [0, 0, -1, 1]


def dfs(n_x, n_y):
    global count
    global visit
    global find
    for a, b in zip(x_list, y_list):
        if find:
            return
        if arr[n_x + a][n_y + b] == 2:
            find = True
            return
        elif arr[n_x + a][n_y + b] == 0 and visit[n_x + a][n_y + b] == 0:
            visit[n_x + a][n_y + b] = 1
            dfs(n_x + a, n_y + b)
    return


answer = 0
while True:
    to_delete = []
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                check = 0
                for x, y in zip(x_list, y_list):
                    if arr[i + x][j + y] in [0, 2]:
                        check += 1
                if check >= 2:
                    count = 0
                    for x, y in zip(x_list, y_list):
                        if count >= 2:
                            break
                        if arr[i + x][j + y] == 2:
                            count += 1
                        elif arr[i + x][j + y] == 0:
                            visit = [[0 for _ in range(m)] for _ in range(n)]
                            visit[i][j] = 1
                            visit[i + x][j + y] = 1
                            find = False
                            dfs(i + x, j + y)
                            if find:
                                count += 1
                    if count >= 2:
                        to_delete.append((i, j))
    if len(to_delete) == 0:
        break
    for i, j in to_delete:
        arr[i][j] = 2
    answer += 1
print(answer)
