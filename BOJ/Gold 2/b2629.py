import sys

n = int(sys.stdin.readline())
chu = [0] + list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
bead = list(map(int, sys.stdin.readline().split()))
total = sum(chu)
dp = [[0 for _ in range(total + 1)] for _ in range(n + 1)]
dp[0][0] = 1
for i in range(1, n + 1):
    now = chu[i]
    for j in range(0, total + 1):
        if j >= now:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - now])
        else:
            dp[i][j] = dp[i - 1][j]
answer = []
for b in bead:
    for i in range(total + 1):
        if dp[-1][i] == 1:
            idx = i + b
            if idx > total:
                answer.append('N')
                break
            if dp[-1][idx] == 1:
                answer.append('Y')
                break
print(*answer)
