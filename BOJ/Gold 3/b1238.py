import sys
import heapq
from math import inf

n, m, x = map(int, sys.stdin.readline().split())

arr = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e, t = map(int, sys.stdin.readline().split())
    arr[s].append([e, t])


def dijkstra(start):
    global arr
    global dp
    heap = []
    heapq.heappush(heap, (0, start))
    while heap:
        wei, now = heapq.heappop(heap)
        for next_node, next_w in arr[now]:
            w = wei + next_w
            if dp[next_node] > w:
                dp[next_node] = w
                heapq.heappush(heap, (w, next_node))


answer = [0 for _ in range(n + 1)]
for i in range(1, n + 1):
    dp = [inf for _ in range(n + 1)]
    dp[i] = 0
    dijkstra(i)
    if i == x:
        for j in range(1, n + 1):
            answer[j] += dp[j]
    answer[i] += dp[x]
print(max(answer))
