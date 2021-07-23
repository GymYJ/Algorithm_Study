import sys
from math import sqrt


def find(v):
    global parent
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]


def union(v, u):
    global parent, rank
    root1 = find(v)
    root2 = find(u)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]:
                rank[root2] += 1


n, m = map(int, sys.stdin.readline().split())
loc = [[0, 0]]
for _ in range(n):
    loc.append(list(map(int, sys.stdin.readline().split())))
graph = []
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        leng = sqrt((loc[i][0] - loc[j][0]) ** 2 + (loc[i][1] - loc[j][1]) ** 2)
        graph.append((leng, i, j))
graph.sort()
parent = {i: i for i in range(1, n + 1)}
rank = {i: 0 for i in range(1, n + 1)}
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    union(a, b)
answer = 0
for edge in graph:
    weight, v, u = edge
    if find(v) != find(u):
        union(v, u)
        answer += weight
print('%.2f' % answer)
