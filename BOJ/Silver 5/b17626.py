from math import sqrt, floor


def main():
    n = int(input())
    dp = [0 for _ in range(n + 2)]
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    for i in range(4, n + 2):
        num = i
        temp = sqrt(num)
        if int(temp) == temp:
            dp[i] = 1
        else:
            j = floor(temp)
            dp[i] = min([dp[num - (j - i) ** 2] for i in range(j // 3, j)]) + 1
    print(dp[n])


if __name__ == '__main__':
    main()
