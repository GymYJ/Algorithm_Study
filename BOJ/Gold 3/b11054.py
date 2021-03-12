import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
dp = [0 for _ in range(n)]
dp[0] = 1
for i in range(1, n):
    biggest = 0
    for j in range(0, i):
        if arr[j] < arr[i] and dp[j] > biggest:
            biggest = dp[j]
    dp[i] = biggest + 1
arr.reverse()
reverse_dp = [0 for _ in range(n)]
reverse_dp[0] = 1
for i in range(1, n):
    biggest = 0
    for j in range(0, i):
        if arr[j] < arr[i] and reverse_dp[j] > biggest:
            biggest = reverse_dp[j]
    reverse_dp[i] = biggest + 1
answer = 0
for i in range(n):
    answer = max(answer, dp[i] + reverse_dp[n - i - 1] - 1)
print(answer)
