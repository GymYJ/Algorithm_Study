import sys
from math import inf


def floyd():
    global n, pay, route
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if pay[i][j] > pay[i][k] + pay[k][j]:
                    pay[i][j] = pay[i][k] + pay[k][j]
                    if route[i][k][-1] == route[k][j][0]:
                        route[i][j] = route[i][k] + route[k][j][1:]
                    else:
                        route[i][j] = route[i][k] + route[k][j]


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
pay = [[inf for _ in range(n + 1)] for _ in range(n + 1)]
route = [[[inf] for i in range(n + 1)] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    if pay[a][b] > c:
        pay[a][b] = c
        route[a][b] = [a, b]
for i in range(1, n + 1):
    pay[i][i] = 0
floyd()
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if pay[i][j] == inf:
            pay[i][j] = 0
for p in pay[1:]:
    print(*p[1:])
for r in route[1:]:
    for i in r[1:]:
        if i[0] == inf:
            print(0)
        else:
            print(len(i), *i)
