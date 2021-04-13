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
length = max(dp)
answer = []
index = n
for i in range(length, 0, -1):
    while True:
        index -= 1
        if dp[index] == i:
            answer.append(arr[index])
            break
print(length)
print(' '.join(list(map(str, reversed(answer)))))
