import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
graph = {i: [] for i in range(1, n + 1)}
arr = ['']
for _ in range(n):
    arr.append(sys.stdin.readline().strip())
a, b = map(int, sys.stdin.readline().split())
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        check = 0
        is_p = True
        for idx in range(k):
            if arr[i][idx] != arr[j][idx]:
                check += 1
            if check > 1:
                is_p = False
                break
        if is_p and check == 1:
            graph[i].append(j)
            graph[j].append(i)

visit = [0 for _ in range(n + 1)]
visit[a] = 1
q = deque([[a]])
while q:
    now = q.popleft()
    if now[-1] == b:
        print(*now)
        sys.exit()
    for num in graph[now[-1]]:
        if visit[num] == 0:
            visit[num] = 1
            q.append(now + [num])
print(-1)
