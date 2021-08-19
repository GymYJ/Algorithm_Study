import sys


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
univ = ['0'] + list(sys.stdin.readline().split())
graph = []
for _ in range(m):
    u, v, d = map(int, sys.stdin.readline().split())
    if univ[u] != univ[v]:
        graph.append((d, u, v))
graph.sort()
parent = {i: i for i in range(1, n + 1)}
rank = {i: 0 for i in range(1, n + 1)}
length = 0
visit = [0 for _ in range(n + 1)]
for edge in graph:
    weight, v, u = edge
    if find(v) != find(u):
        union(v, u)
        length += weight
        visit[v] = 1
        visit[u] = 1

print(length if sum(visit) == n else -1)
