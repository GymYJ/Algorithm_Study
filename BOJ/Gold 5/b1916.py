import sys
import heapq
from math import inf

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
arr = [[] for _ in range(n + 1)]
for _ in range(m):
    start, end, charge = map(int, sys.stdin.readline().split())
    arr[start].append([end, charge])
start, end = map(int, sys.stdin.readline().split())
dp = [inf for _ in range(n + 1)]


def dijkstra(s):
    global arr, dp
    heap = []
    heapq.heappush(heap, (0, s))
    while heap:
        wei, now = heapq.heappop(heap)
        if dp[now] < wei:
            continue
        for next_node, next_wei in arr[now]:
            w = next_wei + wei
            if dp[next_node] > w:
                dp[next_node] = w
                heapq.heappush(heap, (w, next_node))


dijkstra(start)
print(dp[end])
