import sys

n, m = map(int, sys.stdin.readline().split())
boy = [0] + list(map(int, sys.stdin.readline().split()))
girl = [0] + list(map(int, sys.stdin.readline().split()))
boy.sort()
girl.sort()
if n > m:
    boy, girl = girl, boy
    n, m = m, n
dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(i, m - (n - i - 1)):
        if i == j:
            dp[i][j] = dp[i - 1][j - 1] + abs(boy[i] - girl[j])
        else:
            dp[i][j] = min(dp[i - 1][j - 1] + abs(boy[i] - girl[j]), dp[i][j - 1])
print(dp[-1][-1])
