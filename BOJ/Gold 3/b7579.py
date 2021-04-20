import sys
from math import inf

n, m = map(int, sys.stdin.readline().split())
A = [0] + list(map(int, sys.stdin.readline().split()))
c = [0] + list(map(int, sys.stdin.readline().split()))
total = sum(c)
dp = [[0 for _ in range(total + 1)] for _ in range(n + 1)]
answer = total
for i in range(1, n + 1):
    for j in range(1, total + 1):
        if j < c[i]:  # 현재 앱을 비활성화할만큼의 cost가 충분하지 않을 경우
            dp[i][j] = dp[i - 1][j]
        else:
            # 같은 cost 내에서 현재 앱을 끈 뒤의 byte와 현재 앱을 끄지 않은 byte를 비교
            dp[i][j] = max(A[i] + dp[i - 1][j - c[i]], dp[i - 1][j])
        if dp[i][j] >= m:
            answer = min(answer, j)
print(answer if m != 0 else 0)
