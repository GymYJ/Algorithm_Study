import sys


def get_parent(x):
    if parent[x] == x:
        return x
    p = get_parent(parent[x])
    parent[x] = p
    return p


def union(x, y):
    x = get_parent(x)
    y = get_parent(y)

    if x != y:
        parent[y] = x


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
parent = {i: i for i in range(1, n + 1)}
for i in range(1, n + 1):
    arr = list(map(int, sys.stdin.readline().split()))
    for j, is_connect in enumerate(arr, start=1):
        if is_connect:
            union(i, j)
plan = list(map(int, sys.stdin.readline().split()))
now = plan[0]
for next_node in plan[1:]:
    if get_parent(now) != get_parent(next_node):
        print('NO')
        sys.exit()
print('YES')
