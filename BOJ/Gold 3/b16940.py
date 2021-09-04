import sys
from collections import deque

n = int(sys.stdin.readline())
graph = {i: [] for i in range(1, n + 1)}
for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
check = deque(list(map(int, sys.stdin.readline().split())))
if check.popleft() != 1:
    print(0)
    sys.exit()
visit = [0 for _ in range(n + 1)]
is_p = True
visit[1] = 1
q = deque([1])
while q:
    now = q.popleft()
    while check:
        num = check[0]
        if num in graph[now]:
            if visit[num] == 0:
                visit[num] = 1
                q.append(num)
                check.popleft()
        else:
            break
    for num in graph[now]:
        if visit[num] == 0:
            print(0)
            sys.exit()
print(1)
