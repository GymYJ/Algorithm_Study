import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))
visit = [[0 for _ in range(m)] for _ in range(n)]
num = 1
move = [[-1, 0], [1, 0], [0, -1], [0, 1]]
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and visit[i][j] == 0:
            arr[i][j] = num
            q = deque([[i, j]])
            visit[i][j] = 1
            while q:
                x, y = q.popleft()
                for dx, dy in move:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 1 and visit[nx][ny] == 0:
                        arr[nx][ny] = num
                        visit[nx][ny] = 1
                        q.append([nx, ny])
            num += 1
island = num - 1

graph = []
for i in range(n):
    for j in range(m):
        if arr[i][j] != 0:
            temp = []
            for dx, dy in move:
                nx, ny = i + dx, j + dy
                if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0:
                    temp.append([nx, ny, dx, dy, 1])
            q = deque(temp)
            num = arr[i][j]
            while q:
                x, y, dx, dy, count = q.popleft()
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m:
                    if arr[nx][ny] == 0:
                        q.append([nx, ny, dx, dy, count + 1])
                    elif arr[nx][ny] != num:
                        if count >= 2:
                            graph.append([count, num, arr[nx][ny]])
graph.sort()
parent = {i: i for i in range(island + 1)}
rank = {i: 0 for i in range(island + 1)}


def find(v):
    global parent
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]


def union(v, u):
    global parent, rank
    root1 = parent[v]
    root2 = parent[u]

    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]:
                rank[root2] += 1


answer = 0
for edge in graph:
    weight, v, u = edge
    if find(v) != find(u):
        union(v, u)
        answer += weight

p = find(island)
mst = True
for i in range(1, island + 1):
    if find(i) != p:
        mst = False
print(answer if mst else -1)
