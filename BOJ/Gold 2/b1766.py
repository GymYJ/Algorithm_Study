import sys
import heapq

n, m = map(int, sys.stdin.readline().split())
h = []
seq = {i: [] for i in range(1, n + 1)}
degree = {i: 0 for i in range(1, n + 1)}
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    seq[a].append(b)
    degree[b] += 1
for i in range(1, n + 1):
    if degree[i] == 0:
        h.append(i)
heapq.heapify(h)
answer = []
while h:
    now = heapq.heappop(h)
    answer.append(now)
    for i in seq[now]:
        degree[i] -= 1
        if degree[i] == 0:
            heapq.heappush(h, i)
print(*answer)
