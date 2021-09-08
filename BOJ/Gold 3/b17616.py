import sys
from collections import deque

n, m, x = map(int, sys.stdin.readline().split())
dic = {i: {'up': [], 'down': []} for i in range(1, n + 1)}
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    dic[a]['down'].append(b)
    dic[b]['up'].append(a)
up_count = 0
down_count = 0
visit = [0 for _ in range(n + 1)]
visit[x] = 1
q = deque([x])
while q:
    now = q.popleft()
    for i in dic[now]['up']:
        if visit[i] == 0:
            visit[i] = 1
            q.append(i)
            up_count += 1
q = deque([x])
while q:
    now = q.popleft()
    for i in dic[now]['down']:
        if visit[i] == 0:
            visit[i] = 1
            q.append(i)
            down_count += 1
print(1 + up_count, n - down_count)
