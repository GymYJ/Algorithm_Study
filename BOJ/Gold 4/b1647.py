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
        if rank[root1] < rank[root2]:
            parent[root1] = root2
        else:
            parent[root2] = root1
            if rank[root1] == rank[root2]:
                rank[root1] += 1


n, m = map(int, sys.stdin.readline().split())
load = []
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    load.append((c, a, b))
load.sort()
parent = {i: i for i in range(1, n + 1)}
rank = {i: 0 for i in range(1, n + 1)}

mst = []
for cost, a, b in load:
    if find(a) != find(b):
        union(a, b)
        mst.append(cost)
print(sum(mst) - max(mst))
