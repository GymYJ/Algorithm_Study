import sys

n = int(sys.stdin.readline())
p = [0] + list(map(int, sys.stdin.readline().split()))
dp = [0 for _ in range(n + 1)]
dp[1] = p[1]
for i in range(2, n + 1):
    arr = []
    for j in range(i - 1, -1, -1):
        arr.append(dp[j] + p[i - j])
        if i - j == len(p):
            break
    dp[i] = max(arr)
print(dp[n])
