import sys

n = int(sys.stdin.readline())
arr = list(sys.stdin.readline().strip())
dp = [[-1 for _ in range(n)] for _ in range(n)]
for length in range(n):
    for start in range(n):
        end = start + length
        if end >= n:
            break
        if start == end:
            dp[start][end] = 0
            continue
        elif start + 1 == end:
            if arr[start] == arr[end]:
                dp[start][end] = 0
            else:
                dp[start][end] = 1
            continue
        else:
            if arr[start] == arr[end]:
                dp[start][end] = dp[start + 1][end - 1]
            else:
                dp[start][end] = min(dp[start][end - 1] + 1, dp[start + 1][end] + 1)
print(dp[0][n - 1])
