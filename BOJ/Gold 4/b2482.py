import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
answer = 0

dp = [[0 for _ in range(n + 1)] for _ in range(k + 1)]
dp2 = [0 for _ in range(n + 1)]
for i in range(1, n + 1):
    dp[1][i] = 1
    dp2[i] = i
for j in range(2, k + 1):
    temp = [0 for _ in range(n + 1)]
    for i in range(2, n + 1):
        if i == n:
            dp[j][i] = dp[j][i - 1]
        else:
            dp[j][i] = dp2[i - 2]
        temp[i] = (temp[i - 1] + dp[j][i]) % 1000000003
    dp2 = temp
print(dp2[-1])
