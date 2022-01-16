import sys
from collections import deque

n = int(sys.stdin.readline())
colors = [0] + list(map(int, sys.stdin.readline().split()))
graph = {i: [] for i in range(1, n + 1)}
visit = [0 for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
answer = 0
q = deque([[1, 0]])
visit[1] = 1
while q:
    now, c = q.popleft()
    if colors[now] != c:
        answer += 1
        c = colors[now]
    for i in graph[now]:
        if visit[i] == 0:
            visit[i] = 1
            q.append([i, c])
print(answer)
