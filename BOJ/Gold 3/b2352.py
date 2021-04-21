import sys
from bisect import bisect

n = int(sys.stdin.readline())
link = list(map(int, sys.stdin.readline().split()))
dp = [link[0]]
for i in range(1, n):
    if dp[-1] < link[i]:
        dp.append(link[i])
    else:
        dp[bisect(dp, link[i])] = link[i]
print(len(dp))
