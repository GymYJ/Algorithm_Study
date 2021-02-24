import sys


def main():
    n = int(sys.stdin.readline())
    arr = [[0, 0, 0]]
    for _ in range(n):
        arr.append(list(map(int, sys.stdin.readline().split())))
    dp = [[0, 0, 0] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(3):
            if j == 0:
                dp[i][j] = min(dp[i - 1][1], dp[i - 1][2]) + arr[i][j]
            elif j == 1:
                dp[i][j] = min(dp[i - 1][0], dp[i - 1][2]) + arr[i][j]
            else:
                dp[i][j] = min(dp[i - 1][0], dp[i - 1][1]) + arr[i][j]
    print(min(dp[n]))


if __name__ == '__main__':
    main()
