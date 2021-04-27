import sys
from collections import deque

n = int(sys.stdin.readline())
node = {}
graph = {i: [] for i in range(1, n + 1)}
degree = [0 for _ in range(n + 1)]
time = [0 for _ in range(n + 1)]
for i in range(1, n + 1):
    temp = list(map(int, sys.stdin.readline().split()))
    node[i] = temp[0]
    degree[i] = temp[1]
    for j in range(temp[1]):
        graph[temp[j + 2]].append(i)
first = [i for i in range(1, n + 1) if degree[i] == 0]
for i in first:
    time[i] = node[i]
q = deque([(i, time[i]) for i in first])
while q:
    now, t = q.popleft()
    for i in graph[now]:
        time[i] = max(time[i], node[i] + t)
        degree[i] -= 1
        if degree[i] == 0:
            q.append((i, time[i]))
print(max(time))
