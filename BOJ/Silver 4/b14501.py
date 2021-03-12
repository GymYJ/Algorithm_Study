def main():
    n = int(input())
    work = [[0, 0]]
    for _ in range(n):
        work.append(list(map(int, input().split())))
    dp = [0 for _ in range(n + 1)]
    for i in range(1, n + 1):
        t, p = work[i]
        if i + t - 1 <= n:
            if dp[i + t - 1] < dp[i - 1] + p:
                dp[i + t - 1] = dp[i - 1] + p
        if dp[i] < dp[i - 1]:
            dp[i] = dp[i - 1]
    print(dp[n])


if __name__ == '__main__':
    main()
