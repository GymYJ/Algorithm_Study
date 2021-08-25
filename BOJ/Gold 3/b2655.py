import sys

n = int(sys.stdin.readline())
bricks = [(0, 0, 0, 0)]

for idx in range(1, n + 1):
    a, h, w = map(int, sys.stdin.readline().split())
    bricks.append((idx, a, h, w))

bricks.sort(key=lambda x: x[3])

dp = [0] * (n + 1)
for i in range(1, n + 1):
    for j in range(0, i):
        if bricks[i][1] > bricks[j][1]:
            dp[i] = max(dp[i], dp[j] + bricks[i][2])

max_value = max(dp)
idx = n
result = []

while idx > 0:
    if max_value == dp[idx]:
        result.append(bricks[idx][0])
        max_value -= bricks[idx][2]
    idx -= 1

result.reverse()
print(len(result))
for r in result:
    print(r)
