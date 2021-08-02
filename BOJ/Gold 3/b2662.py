import sys

n, m = map(int, sys.stdin.readline().split())
arr = [[0] * (m + 1)]
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))
dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
combi = [[[0] * (m + 1) for _ in range(m + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        for k in range(i + 1):
            if dp[i][j] < dp[i - k][j - 1] + arr[k][j]:
                dp[i][j] = dp[i - k][j - 1] + arr[k][j]
                combi[i][j] = combi[i - k][j - 1][:j] + [k] + [0] * (m - j)
print(dp[n][m])
print(*combi[n][m][1:])
