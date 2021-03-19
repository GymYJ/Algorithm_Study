import sys
from collections import deque

k = int(sys.stdin.readline())
for _ in range(k):
    v, e = map(int, sys.stdin.readline().split())
    dic = {i: [] for i in range(1, v + 1)}
    for _ in range(e):
        a, b = map(int, sys.stdin.readline().split())
        dic[a].append(b)
        dic[b].append(a)
    visit = [0 for _ in range(v + 1)]
    color = [0 for _ in range(v + 1)]
    isTrue = True
    for i in range(1, v + 1):
        if visit[i] == 0:
            visit[i] = 1
            q = deque([i])
            color[i] = 1
            while q:
                now = q.popleft()
                for a in dic[now]:
                    if color[a] == 0:
                        visit[a] = 1
                        q.append(a)
                        color[a] = color[now] * (-1)
                    elif color[a] == color[now]:
                        isTrue = False
                        break
                if not isTrue:
                    break
        if not isTrue:
            break
    if isTrue:
        print('YES')
    else:
        print('NO')
