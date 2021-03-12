n, k = input().split()
n, k = int(n), int(k)
if k <= n:
    print(n - k)
else:
    dp = [0 for _ in range(k + 1)]
    for i in range(n + 1):
        dp[i] = n - i
    for i in range(n + 1, k + 1):
        if i % 2 == 0:
            dp[i] = min(dp[i - 1] + 1, dp[i // 2] + 1)
        else:
            dp[i] = min(dp[i - 1] + 1, dp[(i - 1) // 2] + 2, dp[(i + 1) // 2] + 2)
    print(dp[k])