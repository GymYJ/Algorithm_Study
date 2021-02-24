import sys
import heapq
from math import inf

v, e = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline())
s = [[] for _ in range(v + 1)]
dp = [inf for _ in range(v + 1)]
heap = []


def dijkstra(start):
    dp[start] = 0
    heapq.heappush(heap, [0, start])
    while heap:
        w, n = heapq.heappop(heap)
        for n_n, wei in s[n]:
            n_w = wei + w
            if n_w < dp[n_n]:
                dp[n_n] = n_w
                heapq.heappush(heap, [n_w, n_n])


for _ in range(e):
    u, v, w = map(int, sys.stdin.readline().split())
    s[u].append([v, w])
dijkstra(k)
for i in dp[1:]:
    print(i if i != inf else "INF")
