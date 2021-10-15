import sys


def find(x):
    global dp
    left = 0
    right = len(dp)
    while left < right:
        mid = (left + right) // 2
        if dp[mid][0] < x:
            left = mid + 1
        else:
            right = mid
    return left


n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
dp = [[0, 0]]
dp2 = [0 for _ in range(n + 1)]
max_value = 0
for i, num in enumerate(arr, start=1):
    if dp[-1][0] < num:
        dp.append([num, i])
        max_value += 1
        dp2[i] = max_value
    else:
        j = find(num)
        dp2[i] = dp2[dp[j][1]]
        dp[j] = [num, i]
print(n - (len(dp) - 1))
