import sys
import heapq
from math import inf

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
arr = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e, f = map(int, sys.stdin.readline().split())
    arr[s].append([e, f])
s, e = map(int, sys.stdin.readline().split())
dp = [[inf, [i]] for i in range(n + 1)]
dp[s][0] = 0


def dijkstra(start):
    global arr
    global dp
    h = []
    heapq.heappush(h, (0, start, [start]))
    while h:
        fee, now, route = heapq.heappop(h)
        for next_node, next_fee in arr[now]:
            fe = fee + next_fee
            if dp[next_node][0] > fe:
                dp[next_node][0] = fe
                dp[next_node][1] = route + [next_node]
                heapq.heappush(h, (fe, next_node, route + [next_node]))


dijkstra(s)
print(dp[e][0])
print(len(dp[e][1]))
print(' '.join(map(str, dp[e][1])))
