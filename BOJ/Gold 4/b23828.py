import sys
from collections import defaultdict

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
dic = defaultdict(int)
for a in arr:
    dic[a] += a
values = [0] + list(dic.values())
dp = [[0 for _ in range(m + 1)] for _ in range(len(values))]
for i in range(len(values)):
    dp[i][0] = 1
for i in range(1, len(values)):
    for j in range(1, m + 1):
        dp[i][j] = (dp[i - 1][j] + dp[i - 1][j - 1] * values[i]) % 1000000007
print(dp[-1][m])
