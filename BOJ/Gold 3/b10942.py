import sys

n = int(sys.stdin.readline())
arr = [0] + list(map(int, sys.stdin.readline().split()))
dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
for L in range(0, n):
    for start in range(1, n + 1):
        end = start + L
        if end > n:
            break
        if start == end:
            dp[start][end] = 1
            continue
        elif start + 1 == end:
            if arr[start] == arr[end]:
                dp[start][end] = 1
                continue
        elif arr[start] == arr[end] and dp[start + 1][end - 1]:
            dp[start][end] = 1
m = int(sys.stdin.readline())
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    print(dp[a][b])
