import sys

n, s, m = map(int, sys.stdin.readline().split())
v = list(map(int, sys.stdin.readline().split()))

dp = {s}
dp2 = set()
for i in v:
    for j in dp:
        if j + i <= m:
            dp2.add(j + i)
        if j - i >= 0:
            dp2.add(j - i)
    dp = dp2
    dp2 = set()

if len(dp) == 0:
    print(-1)
else:
    print(max(dp))
