import sys


def get_parent(x):
    if parent[x] == x:
        return x
    prt = get_parent(parent[x])
    parent[x] = prt
    return prt


def union(x):
    x = get_parent(x)
    y = get_parent(x - 1)

    if x != y:
        parent[x] = y


g = int(sys.stdin.readline())
p = int(sys.stdin.readline())
parent = {i: i for i in range(g + 1)}
gate = [0 for _ in range(g + 1)]
check = True
for _ in range(p):
    gi = int(sys.stdin.readline())
    if check:
        pa = get_parent(gi)
        while gate[pa] == 1:
            pa = get_parent(pa - 1)
        if pa == 0:
            check = False
        else:
            gate[pa] = 1
            union(pa)
print(gate.count(1))
