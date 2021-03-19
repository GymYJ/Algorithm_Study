import sys

v, e = map(int, sys.stdin.readline().split())
graph = []
for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    graph.append((c, a, b))
graph.sort()
parent = {i: i for i in range(1, v + 1)}
rank = {i: 0 for i in range(1, v + 1)}


# 해당 정점의 최상위 정점을 찾는다.
def find(v):
    global parent
    if parent[v] != v:
        parent[v] = find(parent[v])

    return parent[v]


# 두 정점을 연결한다.
def union(v, u):
    global parent, rank
    root1 = find(v)
    root2 = find(u)

    if root1 != root2:
        # 짧은 트리의 루트가 긴 트리의 루트를 가리키게 만드는 것이 좋다.
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]:
                rank[root2] += 1


def kruskal():
    global graph
    mst = []

    for edge in graph:
        weight, v, u = edge

        if find(v) != find(u):
            union(v, u)
            mst.append(edge)

    return mst


mst = kruskal()
answer = 0
for m in mst:
    answer += m[0]
print(answer)
