import sys

n = int(sys.stdin.readline())
task = [[] for _ in range(1001)]
last = 1
for _ in range(n):
    d, w = map(int, sys.stdin.readline().split())
    task[d].append(w)
    last = max(last, d)
dp = [0 for _ in range(last + 2)]
to_do = []
for i in range(last, 0, -1):
    to_do = task[i] + to_do
    if len(to_do) == 0:
        dp[i] = dp[i + 1]
        continue
    most = max(to_do)
    dp[i] = dp[i + 1] + most
    to_do.remove(most)
print(dp[1])
