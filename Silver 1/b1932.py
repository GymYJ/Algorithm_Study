def main():
    n = int(input())
    tr = []
    for _ in range(n):
        tr.append(list(map(int, input().split())))
    dp = [tr[0]]
    for i in range(1, n):
        temp = []
        for j in range(i + 1):
            if j == 0:
                temp.append(dp[i - 1][j] + tr[i][j])
            elif j == i:
                temp.append(dp[i - 1][j - 1] + tr[i][j])
            else:
                temp.append(max(dp[i - 1][j - 1], dp[i - 1][j]) + tr[i][j])
        dp.append(temp)
    print(max(dp[n - 1]))


if __name__ == '__main__':
    main()
