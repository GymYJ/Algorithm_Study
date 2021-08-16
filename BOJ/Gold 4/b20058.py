import sys
import copy


def dfs(x, y):
    global arr, move, visit, biggest
    size = 1
    for dx, dy in move:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 2 ** n and 0 <= ny < 2 ** n and arr[nx][ny] > 0 and visit[nx][ny] == 0:
            visit[nx][ny] = 1
            size += dfs(nx, ny)
    return size


sys.setrecursionlimit(10000)
n, q = map(int, sys.stdin.readline().split())
arr = []
for _ in range(2 ** n):
    arr.append(list(map(int, sys.stdin.readline().split())))
move = [[-1, 0], [1, 0], [0, -1], [0, 1]]
for L in list(map(int, sys.stdin.readline().split())):
    for i in range(0, 2 ** n, 2 ** L):
        for j in range(0, 2 ** n, 2 ** L):
            tmp = [arr[k][j:j + 2 ** L] for k in range(i, i + 2 ** L)]
            for k in range(2 ** L):
                for l in range(2 ** L):
                    arr[i + l][j + 2 ** L - 1 - k] = tmp[k][l]
    new_arr = copy.deepcopy(arr)
    for x in range(2 ** n):
        for y in range(2 ** n):
            if arr[x][y] > 0:
                count = 0
                for dx, dy in move:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < 2 ** n and 0 <= ny < 2 ** n and arr[nx][ny] > 0:
                        count += 1
                if count <= 2:
                    new_arr[x][y] -= 1
    arr = new_arr

print(sum(map(sum, arr)))
visit = [[0 for _ in range(2 ** n)] for _ in range(2 ** n)]
biggest = 0
for i in range(2 ** n):
    for j in range(2 ** n):
        if arr[i][j] > 0:
            visit[i][j] = 1
            biggest = max(biggest, dfs(i, j))
print(biggest)
