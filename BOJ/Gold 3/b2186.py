import sys
from collections import deque

n, m, k = map(int, sys.stdin.readline().split())
arr = []
for _ in range(n):
    arr.append(list(sys.stdin.readline().strip()))
word = list(sys.stdin.readline().strip())
idx = len(word) - 1
dp = [[[0 for _ in range(idx + 1)] for _ in range(m)] for _ in range(n)]
char = word[idx]
q = deque()
for i in range(n):
    for j in range(m):
        if arr[i][j] == char:
            dp[i][j][idx] = 1
            q.append((i, j))
move = [[-1, 0], [1, 0], [0, -1], [0, 1]]
for i in range(idx - 1, -1, -1):
    char = word[i]
    next_q = set()
    while q:
        x, y = q.popleft()
        for dx, dy in move:
            for a in range(1, k + 1):
                nx, ny = x + dx * a, y + dy * a
                if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == char:
                    dp[nx][ny][i] += dp[x][y][i + 1]
                    next_q.add((nx, ny))
    q = deque(list(next_q))
answer = 0
for i in range(n):
    for j in range(m):
        answer += dp[i][j][0]
print(answer)
