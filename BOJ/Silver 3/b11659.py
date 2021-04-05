import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
dp = [0]
num = 0
for i in arr:
    num += i
    dp.append(num)
for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    print(dp[j] - dp[i - 1])
