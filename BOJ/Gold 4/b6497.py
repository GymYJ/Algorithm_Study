import sys


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


while True:
    m, n = map(int, sys.stdin.readline().split())
    if m == 0 and n == 0:
        break
    arr = []
    for _ in range(n):
        x, y, z = map(int, sys.stdin.readline().split())
        arr.append([z, x, y])
    arr.sort()
    parent = {i: i for i in range(m)}
    rank = {i: 0 for i in range(m)}
    mst = []
    no_link = []
    for i in arr:
        wei, x, y = i
        x = find(x)
        y = find(y)
        if x != y:
            union(x, y)
            mst.append(wei)
        else:
            no_link.append(wei)
    print(sum(no_link))
