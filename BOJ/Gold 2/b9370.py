import sys
import heapq
from math import inf


def dijkstra(start):
    global arr, dp, route
    h = []
    heapq.heappush(h, (0, start))
    while h:
        wei, now = heapq.heappop(h)
        for next_node, next_wei in arr[now]:
            w = wei + next_wei
            if dp[next_node] > w:
                dp[next_node] = w
                route[next_node] = route[now].copy()
                route[next_node].add((now, next_node))
                heapq.heappush(h, (w, next_node))
            elif dp[next_node] == w:
                route[next_node] = route[next_node].union(route[now])
                route[next_node].add((now, next_node))


T = int(sys.stdin.readline())
for _ in range(T):
    n, m, t = map(int, sys.stdin.readline().split())
    s, g, h = map(int, sys.stdin.readline().split())
    arr = [[] for _ in range(n + 1)]
    dp = [inf for _ in range(n + 1)]
    route = [set() for _ in range(n + 1)]
    for _ in range(m):
        a, b, d = map(int, sys.stdin.readline().split())
        arr[a].append([b, d])
        arr[b].append([a, d])
    dp[s] = 0
    dijkstra(s)
    answer = []
    for _ in range(t):
        candi = int(sys.stdin.readline())
        if (g, h) in route[candi] or (h, g) in route[candi]:
            answer.append(candi)
    answer.sort()
    print(*answer)
