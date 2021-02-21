def main():
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(float(input()))
    dp = [0.0 for _ in range(n)]
    dp[0] = arr[0]
    for i in range(1, n):
        dp[i] = max(dp[i - 1] * arr[i], arr[i])
    print('%.3f' % round(max(dp), 3))


if __name__ == '__main__':
    main()
