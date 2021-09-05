import sys

str1 = '.' + sys.stdin.readline().strip()
str2 = '.' + sys.stdin.readline().strip()

dp = [[0 for _ in range(len(str2))] for _ in range(len(str1))]
for i in range(1, len(str1)):
    dp[i][0] = i
for i in range(1, len(str2)):
    dp[0][i] = i
for i in range(1, len(str1)):
    for j in range(1, len(str2)):
        if str1[i] == str2[j]:
            dp[i][j] = dp[i - 1][j - 1]
        else:
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
print(dp[-1][-1])
