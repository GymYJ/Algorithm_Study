import sys


def dfs(start, end):
    global dna, n, dp
    if start >= end:
        return 0
    if dp[start][end] != -1:
        return dp[start][end]
    for i in range(start, end):
        dp[start][end] = max(dp[start][end], dfs(start, i) + dfs(i + 1, end))
    if (dna[start] == 'a' and dna[end] == 't') or (dna[start] == 'g' and dna[end] == 'c'):
        dp[start][end] = max(dp[start][end], dfs(start + 1, end - 1) + 2)
    return dp[start][end]


dna = sys.stdin.readline().strip()
n = len(dna)
dp = [[-1 for _ in range(n)] for _ in range(n)]
dfs(0, n - 1)
print(dp[0][n - 1])
