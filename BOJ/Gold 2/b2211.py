import sys
import heapq
from math import inf

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([b, c])
    graph[b].append([a, c])
dp = [[inf, []] for _ in range(n + 1)]
dp[1][0] = 0

h = []
heapq.heappush(h, [0, 1])
while h:
    w, node = heapq.heappop(h)
    for nn, dw in graph[node]:
        nw = w + dw
        if dp[nn][0] > nw:
            dp[nn][0] = nw
            dp[nn][1] = dp[node][1] + [(node, nn)]
            heapq.heappush(h, [nw, nn])

lines = set()
for _, route in dp:
    lines.update(route)

print(len(lines))
for line in lines:
    print(*line)
