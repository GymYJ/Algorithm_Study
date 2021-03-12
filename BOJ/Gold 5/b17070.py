import sys


def main():
    n = int(sys.stdin.readline())
    house = [[0 for _ in range(n + 1)]]
    for _ in range(n):
        house.append([0] + list(map(int, sys.stdin.readline().split())))
    dp = [[[0, 0, 0] for _ in range(n + 1)] for _ in range(n + 1)]
    dp[1][2][0] = 1
    for i in range(1, n + 1):
        for j in range(3, n + 1):
            if house[i][j] == 0:
                dp[i][j][0] = dp[i][j - 1][0] + dp[i][j - 1][1]
                dp[i][j][2] = dp[i - 1][j][1] + dp[i - 1][j][2]
                if house[i - 1][j] == 0 and house[i][j - 1] == 0:
                    dp[i][j][1] = dp[i - 1][j - 1][0] + dp[i - 1][j - 1][1] + dp[i - 1][j - 1][2]
    print(sum(dp[n][n]))


if __name__ == '__main__':
    main()
