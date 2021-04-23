import sys
from collections import defaultdict, deque


def bfs(w):
    global end, graph, wei, visit
    q = deque([start])
    while q:
        now = q.popleft()
        if now == end:
            return True
        for i in graph[now]:
            if wei[now][i] >= w and visit[i] == 0:
                visit[i] = 1
                q.append(i)
    return False


n, m = map(int, sys.stdin.readline().split())
graph = {i: [] for i in range(1, n + 1)}
wei = {i: defaultdict(int) for i in range(1, n + 1)}
low = 1
high = 1
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    wei[a][b] = max(wei[a][b], c)
    wei[b][a] = max(wei[b][a], c)
    high = max(high, c)
start, end = map(int, sys.stdin.readline().split())
answer = 1
while low <= high:
    mid = (low + high) // 2
    visit = [0] * (n + 1)
    visit[start] = 1
    if bfs(mid):
        answer = mid
        low = mid + 1
    else:
        high = mid - 1
print(answer)
