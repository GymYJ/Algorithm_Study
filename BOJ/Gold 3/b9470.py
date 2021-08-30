import sys
from collections import deque

t = int(sys.stdin.readline())
for _ in range(t):
    k, m, p = map(int, sys.stdin.readline().split())
    seq = [1 for _ in range(m + 1)]
    seq[0] = 0
    graph = {i: [] for i in range(1, m + 1)}
    check = {i: {} for i in range(1, m + 1)}
    for _ in range(p):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        check[b][a] = 0
        seq[b] = 0
    start = []
    for i in range(m + 1):
        if seq[i] == 1:
            start.append(i)
    q = deque(start)
    while q:
        new_q = []
        visit = [0 for _ in range(m + 1)]
        while q:
            now = q.popleft()
            for next_node in graph[now]:
                check[next_node][now] = seq[now]
                is_add = True
                value = 0
                count = 0
                for i in check[next_node]:
                    if check[next_node][i] == 0:
                        is_add = False
                        break
                    else:
                        if value < check[next_node][i]:
                            value = check[next_node][i]
                            count = 1
                        elif value == check[next_node][i]:
                            count += 1
                if is_add:
                    new_q.append(next_node)
                    if count == 1:
                        seq[next_node] = value
                    else:
                        seq[next_node] = value + 1
        q = deque(new_q)
    print(k, seq[m])
