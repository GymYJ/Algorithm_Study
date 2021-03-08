import sys

n = int(sys.stdin.readline())
dp = [1 for _ in range(10)]
for _ in range(2, n + 1):
    dp2 = [0 for _ in range(10)]
    for i in range(10):
        dp2[i] = sum(dp[:i + 1])
    dp = dp2
print(sum(dp) % 10007)
