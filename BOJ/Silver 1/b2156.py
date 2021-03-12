def main():
    n = int(input())
    arr = [0]
    for _ in range(n):
        arr.append(int(input()))
    dp = [0 for i in range(n + 1)]
    dp[1] = arr[1]
    if n > 1:
        dp[2] = arr[1] + arr[2]
        for i in range(3, n + 1):
            dp[i] = max(max(dp[:i - 1]), max(dp[:i - 2]) + arr[i - 1]) + arr[i]
    print(max(dp))


if __name__ == '__main__':
    main()
