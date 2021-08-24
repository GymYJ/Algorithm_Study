import sys


def dfs(now):
    global graph, visit, nodes
    node = 1
    for i in graph[now]:
        if visit[i] == 0:
            visit[i] = 1
            node += dfs(i)
    nodes[now] = node
    return node


sys.setrecursionlimit(1000000)
n, r, q = map(int, sys.stdin.readline().split())
graph = {i: [] for i in range(1, n + 1)}
for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
visit = [0 for _ in range(n + 1)]
nodes = [0 for _ in range(n + 1)]
visit[r] = 1
dfs(r)
for _ in range(q):
    u = int(sys.stdin.readline())
    print(nodes[u])
