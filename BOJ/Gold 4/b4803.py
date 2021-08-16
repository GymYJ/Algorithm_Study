import sys


def dfs(now, before):
    global dic, visit, is_tree
    for i in dic[now]:
        if i != before:
            if visit[i] == 0:
                visit[i] = 1
                dfs(i, now)
            else:
                is_tree = False


case = 1
while True:
    n, m = map(int, sys.stdin.readline().split())
    if n == 0 and m == 0:
        break
    dic = {i: [] for i in range(1, n + 1)}
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        dic[a].append(b)
        dic[b].append(a)
    visit = [0 for _ in range(n + 1)]
    tree = 0
    for i in range(1, n + 1):
        if visit[i] == 0:
            is_tree = True
            visit[i] = 1
            dfs(i, 0)
            if is_tree:
                tree += 1
    if not tree:
        print(f"Case {case}: No trees.")
    elif tree == 1:
        print(f"Case {case}: There is one tree.")
    else:
        print(f"Case {case}: A forest of {tree} trees.")
    case += 1
