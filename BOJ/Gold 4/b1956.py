import sys
import heapq
from math import inf

v, e = map(int, sys.stdin.readline().split())
graph = {i: [] for i in range(1, v + 1)}
for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
answer = inf
for i in range(1, v + 1):
    dp = [inf] * (v + 1)
    heap = []
    heapq.heappush(heap, (0, i))
    while heap:
        wei, now = heapq.heappop(heap)
        if wei > 0 and now == i:
            answer = min(answer, wei)
        for next_node, next_wei in graph[now]:
            w = wei + next_wei
            if answer < w:
                continue
            if dp[next_node] > w:
                dp[next_node] = w
                heapq.heappush(heap, (w, next_node))
print(answer if answer != inf else -1)
