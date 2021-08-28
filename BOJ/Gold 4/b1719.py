import sys
from math import inf


def floyd():
    global dp, chart, n
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if dp[i][j] > dp[i][k] + dp[k][j]:
                    dp[i][j] = dp[i][k] + dp[k][j]
                    chart[i][j] = chart[i][k]


n, m = map(int, sys.stdin.readline().split())
dp = [[inf for _ in range(n + 1)] for _ in range(n + 1)]
chart = [['' for _ in range(n + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    dp[i][i] = 0
    chart[i][i] = '-'
for _ in range(m):
    a, b, wei = map(int, sys.stdin.readline().split())
    if dp[a][b] > wei:
        dp[a][b] = wei
        dp[b][a] = wei
        chart[a][b] = b
        chart[b][a] = a

floyd()

for i in range(1, n + 1):
    print(*chart[i][1:])
