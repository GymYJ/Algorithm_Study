import sys


def floyd():
    global arr_up, arr_down
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if arr_up[i][j] or (arr_up[i][k] and arr_up[k][j]):
                    arr_up[i][j] = 1
                if arr_down[i][j] or (arr_down[i][k] and arr_down[k][j]):
                    arr_down[i][j] = 1


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
arr_up = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
arr_down = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    arr_down[a][b] = 1
    arr_up[b][a] = 1

floyd()
for i in range(1, n + 1):
    print(n - arr_up[i].count(1) - arr_down[i].count(1) - 1)
