import sys
from math import inf

n = int(sys.stdin.readline())
buildings = []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    if y < 0:
        y = -1 * y
    buildings.append((x, y))
buildings.sort()
dp = [inf for _ in range(n + 1)]
dp[0] = 0
for i in range(n):
    top = 0
    for j in range(i, -1, -1):
        top = max(top, buildings[j][1])
        square = max(buildings[i][0] - buildings[j][0], top * 2)
        dp[i + 1] = min(dp[i + 1], dp[j] + square)
print(dp[n])
