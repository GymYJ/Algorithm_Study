import sys

n = int(sys.stdin.readline())
papers = [[0, 0]]
for _ in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    temp.sort()
    papers.append(temp)
papers.sort()
dp = [0 for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(0, i):
        if papers[j][0] <= papers[i][0] and papers[j][1] <= papers[i][1]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))
