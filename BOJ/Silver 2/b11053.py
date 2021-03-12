def main():
    n = int(input())
    arr = list(map(int, input().split()))
    dp = [0 for _ in range(n)]
    dp[0] = 1
    for i in range(1, n):
        biggest = 0
        for j in range(0, i):
            if arr[j] < arr[i] and dp[j] > biggest:
                biggest = dp[j]
        dp[i] = biggest + 1
    print(max(dp))


if __name__ == '__main__':
    main()
