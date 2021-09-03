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
arr = []
for _ in range(m + 1):
    a, b, c = map(int, sys.stdin.readline().split())
    arr.append((c, a, b))
arr.sort(key=lambda x: x[0])
parent = {i: i for i in range(n + 1)}
rank = {i: 0 for i in range(n + 1)}
worst = 0

for edge in arr:
    w, v, u = edge
    if find(v) != find(u):
        union(v, u)
        if w == 0:
            worst += 1

arr.sort(key=lambda x: -x[0])
parent = {i: i for i in range(n + 1)}
rank = {i: 0 for i in range(n + 1)}
best = 0

for edge in arr:
    w, v, u = edge
    if find(v) != find(u):
        union(v, u)
        if w == 0:
            best += 1
print(worst ** 2 - best ** 2)
