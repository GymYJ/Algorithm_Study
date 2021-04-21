import sys
from collections import deque

n = int(sys.stdin.readline())
dic = {i: [] for i in range(1, n + 1)}
for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    dic[a].append(b)
    dic[b].append(a)
parent = [0 for _ in range(n + 1)]
depth = [0 for _ in range(n + 1)]
parent[1] = 1
depth[1] = 1
q = deque([1])
while q:
    now = q.popleft()
    for i in dic[now]:
        if parent[i] == 0:
            parent[i] = now
            depth[i] = depth[now] + 1
            q.append(i)
m = int(sys.stdin.readline())
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    if depth[a] > depth[b]:
        temp = a
        a = b
        b = temp
    while depth[a] < depth[b]:
        b = parent[b]
    if a == b:
        print(a)
    else:
        while a != b:
            a = parent[a]
            b = parent[b]
        print(a)
