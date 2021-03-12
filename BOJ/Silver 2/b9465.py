import sys


def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        arr = []
        for _ in range(2):
            arr.append([0] + list(map(int, sys.stdin.readline().split())))
        dp = [[0 for _ in range(n + 1)], [0 for _ in range(n + 1)]]
        dp[0][1], dp[1][1] = arr[0][1], arr[1][1]
        answer = max(dp[0][1], dp[1][1])
        for i in range(2, n + 1):
            dp[0][i] = max(dp[0][i - 2], dp[1][i - 2], dp[1][i - 1]) + arr[0][i]
            if answer < dp[0][i]:
                answer = dp[0][i]
            dp[1][i] = max(dp[1][i - 2], dp[0][i - 2], dp[0][i - 1]) + arr[1][i]
            if answer < dp[1][i]:
                answer = dp[1][i]
        print(answer)


if __name__ == '__main__':
    main()
