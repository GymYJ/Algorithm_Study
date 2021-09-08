import sys

n = int(sys.stdin.readline())
switch = list(map(int, sys.stdin.readline().split()))
bulb = list(map(int, sys.stdin.readline().split()))
arr = []
for i in range(n):
    arr.append([i + 1, bulb.index(switch[i]) + 1])
dp = [0 for _ in range(n)]
dp[0] = 1
for i in range(1, n):
    max_value = 0
    for j in range(i):
        if arr[i][1] > arr[j][1]:
            max_value = max(max_value, dp[j])
    dp[i] = max_value + 1
maxi = max(dp)
print(maxi)
idx = dp.index(maxi)
answer = [idx]
while maxi > 1 and idx >= 0:
    if dp[idx] == maxi - 1:
        answer.append(idx)
        maxi -= 1
    idx -= 1
answer = [bulb[arr[i][1] - 1] for i in answer]
answer.sort()
print(*answer)
