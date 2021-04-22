import sys
import heapq
from math import inf

move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
num = 1
while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    arr = []
    for _ in range(n):
        arr.append(list(map(int, sys.stdin.readline().split())))
    dp = [[inf for _ in range(n)] for _ in range(n)]
    dp[0][0] = arr[0][0]
    h = []
    heapq.heappush(h, [dp[0][0], 0, 0])
    while h:
        lupy, x, y = heapq.heappop(h)
        for dx, dy in move:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                next_lupy = lupy + arr[nx][ny]
                if dp[nx][ny] > next_lupy:
                    dp[nx][ny] = next_lupy
                    heapq.heappush(h, [next_lupy, nx, ny])
    print(f'Problem {num}:', dp[n - 1][n - 1])
    num += 1
