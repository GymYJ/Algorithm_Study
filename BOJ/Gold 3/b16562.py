import sys


def find(x):
    global parent
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    global pay, parent
    root1 = find(x)
    root2 = find(y)

    if root1 != root2:
        if pay[root1] > pay[root2]:
            parent[root1] = root2
        else:
            parent[root2] = root1


n, m, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
parent = {i: i for i in range(1, n + 1)}
pay = {}
for i in range(1, n + 1):
    pay[i] = arr[i - 1]
for _ in range(m):
    v, w = map(int, sys.stdin.readline().split())

    if find(v) != find(w):
        union(v, w)
for i in range(1, n + 1):
    find(i)
total = 0
for i in set(parent.values()):
    total += pay[i]
print(total if total <= k else 'Oh no')
