import sys


def find(v):
    global parent
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]


def union(u, v):
    global parent, rank
    root1, root2 = find(u), find(v)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]:
                rank[root2] += 1


def kruskal():
    global graph
    mst = []
    for edge in graph:
        wei, u, v = edge
        if find(u) != find(v):
            union(u, v)
            mst.append(edge)
    return mst


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = []
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph.append((c, a, b))
parent = {i: i for i in range(1, n + 1)}
rank = {i: 0 for i in range(1, n + 1)}
graph.sort()
mst = kruskal()
print(sum(i[0] for i in mst))
