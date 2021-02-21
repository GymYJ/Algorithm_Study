def main():
    n, m = list(map(int, input().split()))
    days = [True for _ in range(n + 1)]
    if m:
        for i in list(map(int, input().split())):
            days[i] = False
    dp = [0 for _ in range(n + 1)]
    dp[1] = 10000 if days[1] else 0
    if n > 1:
        dp[2] = dp[1] + 10000 if days[2] else dp[1]
    if n > 2:
        dp[3] = min(dp[2] + 10000, 25000)
    coupon = 0
    for i in range(4, n + 1):
        if days[i]:
            dp[i] = min(dp[i-1] + 10000, dp[i-3] + 25000, dp[i - 4] + 37000, dp[i - 5] + 37000)
        else:
            dp[i] = dp[i - 1]
    print(dp)


if __name__ == '__main__':
    main()
