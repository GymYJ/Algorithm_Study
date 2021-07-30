import sys
import heapq
from math import inf

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
arr = {i: {} for i in range(1, n + 1)}
for _ in range(m):
    s, e, f = map(int, sys.stdin.readline().split())
    if arr[s].get(e):
        arr[s][e] = min(arr[s][e], f)
    else:
        arr[s][e] = f
s, e = map(int, sys.stdin.readline().split())
dp = [inf for i in range(n + 1)]
path = [[] for i in range(n + 1)]
path[s].append(s)
dp[s] = 0


def dijkstra(start):
    global arr
    global dp
    h = []
    heapq.heappush(h, (0, start))
    while h:
        fee, now = heapq.heappop(h)
        for next_node in arr[now]:
            fe = fee + arr[now][next_node]
            if dp[next_node] > fe:
                dp[next_node] = fe
                path[next_node] = path[now] + [next_node]
                heapq.heappush(h, (fe, next_node))


dijkstra(s)
print(dp[e])
print(len(path[e]))
print(*path[e])
