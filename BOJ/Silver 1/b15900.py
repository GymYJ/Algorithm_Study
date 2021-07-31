import sys
from collections import defaultdict, deque

n = int(sys.stdin.readline())
graph = defaultdict(list)
for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
visit = [0 for _ in range(n + 1)]
visit[1] = 1
total = 0
q = deque([[1, 0]])
while q:
    now, c = q.popleft()
    leaf = True
    for num in graph[now]:
        if visit[num] == 0:
            visit[num] = 1
            leaf = False
            q.append([num, c + 1])
    if leaf:
        total += c
print("Yes" if total % 2 == 1 else "No")
