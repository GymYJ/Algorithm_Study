import sys


def find(v):
    global parent
    if v != parent[v]:
        parent[v] = find(parent[v])
    return parent[v]


def union(v, u):
    global parent, rank
    root1 = find(v)
    root2 = find(u)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
            rank[root1] += rank[root2]
        else:
            parent[root1] = root2
            rank[root2] += rank[root1]


t = int(sys.stdin.readline())
for _ in range(t):
    f = int(sys.stdin.readline())
    parent = {}
    rank = {}
    for _ in range(f):
        a, b = sys.stdin.readline().split()
        if not parent.get(a):
            parent[a] = a
            rank[a] = 1
        if not parent.get(b):
            parent[b] = b
            rank[b] = 1
        union(a, b)
        print(rank[find(a)])
