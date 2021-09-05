import sys


def find(n, l, i):
    global answer, dp
    if n == 0:
        return
    if l == 0:
        for _ in range(n):
            answer += '0'
        return
    skip = 0
    for j in range(l + 1):
        skip += dp[n - 1][j]
    if skip >= i:
        answer += '0'
        find(n - 1, l, i)
    else:
        answer += '1'
        find(n - 1, l - 1, i - skip)
    return


N, L, I = map(int, sys.stdin.readline().split())
dp = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
dp[0][0] = 1
dp[1][0] = 1
dp[1][1] = 1
for i in range(2, N + 1):
    dp[i][0] = 1
    dp[i][i] = 1
    for k in range(1, i + 1):
        dp[i][k] = dp[i - 1][k] + dp[i - 1][k - 1]
answer = ''
find(N, L, I)
print(answer)
