import sys

s1 = ' ' + sys.stdin.readline().strip()
s2 = ' ' + sys.stdin.readline().strip()
dp = [[0 for _ in range(len(s1))] for _ in range(len(s2))]
answer = 0
for i in range(1, len(s2)):
    for j in range(1, len(s1)):
        if s1[j] == s2[i]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            answer = max(answer, dp[i][j])
print(answer)
