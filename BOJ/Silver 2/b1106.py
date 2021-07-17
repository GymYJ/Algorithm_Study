import sys
from math import inf

c, n = map(int, sys.stdin.readline().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))
arr.sort(key=lambda x: x[0] / x[1])
dp = [inf for _ in range(c + 101)]
for cost, num in arr:
    i = num + 1
    total = cost
    while i < c:
        for j in range(i - num, i):
            if dp[j] > total:
                dp[j] = total
        i += num
        total += cost
    for j in range(i - num, i):
        if dp[j] > total:
            dp[j] = total
for cost, num in arr:
    for i in range(num + 1, c + 101):
        if dp[i] > dp[i - num] + cost:
            dp[i] = dp[i - num] + cost
print(min(dp[c:]))
