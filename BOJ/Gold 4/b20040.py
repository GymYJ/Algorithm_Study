import sys


def find(x):
    global parent
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    global parent
    x = find(x)
    y = find(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


n, m = map(int, sys.stdin.readline().split())
arr = []
for _ in range(m):
    arr.append(list(map(int, sys.stdin.readline().split())))
parent = {i: i for i in range(n)}
answer = 0
for i in range(m):
    a, b = arr[i]
    if find(a) != find(b):
        union(a, b)
    else:
        answer = i + 1
        break
print(answer)
