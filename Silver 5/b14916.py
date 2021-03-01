import sys


def main():
    n = int(sys.stdin.readline())
    dp = [0 for _ in range(100001)]
    dp[1] = -1
    dp[2] = 1
    dp[3] = -1
    dp[4] = 2
    for i in range(5, n + 1):
        if dp[i - 2] >= 0 and dp[i - 5] >= 0:
            dp[i] = min(dp[i - 2], dp[i - 5]) + 1
        elif dp[i - 5] >= 0:
            dp[i] = dp[i - 5] + 1
        else:
            dp[i] = dp[i - 2] + 1
    print(dp[n])


if __name__ == '__main__':
    main()
