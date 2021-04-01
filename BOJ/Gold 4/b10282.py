import sys
import heapq
from math import inf


def dijkstra(start):
    global arr
    global dp
    h = []
    heapq.heappush(h, (0, start))
    while h:
        wei, now = heapq.heappop(h)
        for next_node, next_wei in arr[now]:
            w = wei + next_wei
            if dp[next_node] > w:
                dp[next_node] = w
                heapq.heappush(h, (w, next_node))


t = int(sys.stdin.readline())
for _ in range(t):
    n, d, c = map(int, sys.stdin.readline().split())
    arr = [[] for _ in range(n + 1)]
    dp = [inf for _ in range(n + 1)]
    for _ in range(d):
        a, b, s = map(int, sys.stdin.readline().split())
        arr[b].append([a, s])
    dp[c] = 0
    dijkstra(c)
    print(sum(1 for i in dp if i != inf), max(i for i in dp if i != inf))
