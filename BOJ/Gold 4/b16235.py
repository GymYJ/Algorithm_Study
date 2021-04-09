import sys
from collections import deque

n, m, k = map(int, sys.stdin.readline().split())
a = []
for _ in range(n):
    a.append(list(map(int, sys.stdin.readline().split())))

tree = [[[] for _ in range(n + 1)] for _ in range(n + 1)]
for _ in range(m):
    x, y, z = map(int, sys.stdin.readline().split())
    tree[x][y].append(z)

ground = [[5 for _ in range(n + 1)] for _ in range(n + 1)]
add = [(-1, -1), (-1, 0), (-1, 1),
       (0, -1), (0, 1),
       (1, -1), (1, 0), (1, 1)]
for _ in range(k):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            new_tree = []
            new_ground = 0
            for age in tree[i][j]:
                if ground[i][j] >= age:
                    ground[i][j] -= age
                    new_tree.append(age + 1)
                else:
                    new_ground += age // 2
            tree[i][j] = new_tree
            ground[i][j] += new_ground
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            now = tree[i][j]
            for age in now:
                if age % 5 == 0:
                    for dx, dy in add:
                        x, y = i + dx, j + dy
                        if 1 <= x <= n and 1 <= y <= n:
                            tree[x][y] = [1] + tree[x][y]
            ground[i][j] += a[i - 1][j - 1]
answer = 0
for t in tree:
    for g in t:
        answer += len(g)
print(answer)
