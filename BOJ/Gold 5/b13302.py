import sys
from math import inf

n, m = list(map(int, sys.stdin.readline().split()))
days = [True for _ in range(n + 1)]
if m:
    for i in list(map(int, sys.stdin.readline().split())):
        days[i] = False
dp = [[inf for _ in range(n + 1)] for _ in range(n + 1)]


def dfs(day, coupon):
    global dp
    global n
    if day > n:
        return 0
    if dp[coupon][day] != inf:
        return dp[coupon][day]
    if not days[day]:
        dp[coupon][day] = dfs(day + 1, coupon)
    else:
        dp[coupon][day] = min(dp[coupon][day], dfs(day + 1, coupon) + 10000,
                              dfs(day + 3, coupon + 1) + 25000, dfs(day + 5, coupon + 2) + 37000)
        if coupon >= 3:
            dp[coupon][day] = min(dp[coupon][day], dfs(day + 1, coupon - 3))
    return dp[coupon][day]


print(dfs(1, 0))
