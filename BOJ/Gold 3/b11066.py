import sys

t = int(sys.stdin.readline())
for _ in range(t):
    k = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    dp = [[0 for _ in range(k)] for _ in range(k)]
    sum_ = [0]
    for num in arr:
        sum_.append(sum_[-1] + num)
    for d in range(1, k):
        for i in range(k - d):
            j = d + i
            dp[i][j] = sys.maxsize
            for l in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][l] + dp[l + 1][j] + sum_[j + 1] - sum_[i])
    print(dp[0][k - 1])
