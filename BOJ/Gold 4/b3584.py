import sys
from collections import deque

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    parent = {i: 0 for i in range(1, n + 1)}
    for _ in range(n - 1):
        a, b = map(int, sys.stdin.readline().split())
        parent[b] = a
    a, b = map(int, sys.stdin.readline().split())
    visit = [0 for _ in range(n + 1)]
    visit[a] = 1
    visit[b] = 1
    answer = 0
    q = deque([a, b])
    while q:
        now = q.popleft()
        if parent[now] == 0:
            continue
        if visit[parent[now]] == 0:
            visit[parent[now]] = 1
            q.append(parent[now])
        else:
            answer = parent[now]
            break
    print(answer)
