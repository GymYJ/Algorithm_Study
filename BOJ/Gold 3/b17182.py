import sys
from collections import deque

n, K = map(int, sys.stdin.readline().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))
route = [[{i, j} for j in range(n)] for i in range(n)]
for k in range(n):
    for i in range(n):
        for j in range(n):
            if arr[i][j] > arr[i][k] + arr[k][j]:
                arr[i][j] = arr[i][k] + arr[k][j]
                route[i][j] = route[i][k].union(route[k][j])
q = deque([[K, 0, route[K][K]]])
answer = sys.maxsize
while q:
    now, t, visit = q.popleft()
    if len(visit) == n:
        answer = min(answer, t)
    for i in range(n):
        if i not in visit:
            q.append([i, t + arr[now][i], visit.union(route[now][i])])
print(answer)
