import sys
from math import inf

n = int(sys.stdin.readline())
d = []
r, c = 0, 0
for _ in range(n):
    r, c = map(int, sys.stdin.readline().split())
    d.append(r)
d.append(c)
dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
for diagonal in range(1, n):  # 구하려는 행렬 사이즈 만큼 반복
    for i in range(1, n - diagonal + 1):  # i 값은 1부터 시작, 반복하는 횟수가 1씩 감소
        j = i + diagonal  # j 값은 우측으로 diagonal 만큼 이동
        dp[i][j] = inf
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + d[i - 1] * d[k] * d[j])
print(dp[1][n])
