import sys


def main():
    n = int(sys.stdin.readline())
    dp = [0 for _ in range(n + 1)]
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    print(dp[n])


if __name__ == '__main__':
    main()
