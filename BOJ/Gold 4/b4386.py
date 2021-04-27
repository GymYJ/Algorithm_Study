import sys
from math import sqrt


def find(x):
    global parent
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    root1 = find(x)
    root2 = find(y)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]:
                rank[root2] += 1


n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    arr.append(list(map(float, sys.stdin.readline().split())))
parent = {i: i for i in range(n)}
rank = {i: 0 for i in range(n)}
graph = []
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        length = sqrt((arr[i][0] - arr[j][0]) ** 2 + (arr[i][1] - arr[j][1]) ** 2)
        graph.append((length, i, j))
graph.sort()
mst = []
for length, x, y in graph:
    if find(x) != find(y):
        union(x, y)
        mst.append(length)
print(round(sum(mst), 2))
