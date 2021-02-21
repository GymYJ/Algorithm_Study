from collections import deque

n = int(input())
com = {i: [] for i in range(1, n + 1)}
m = int(input())
for _ in range(m):
    x, y = input().split()
    com[int(x)].append(int(y))
    com[int(y)].append(int(x))
count = 0
visit = [0] * (n + 1)
visit[1] = 1
q = deque(com[1])
while q:
    now = q.popleft()
    if visit[now] == 0:
        visit[now] = 1
        count += 1
    for i in com[now]:
        if i not in q and visit[i] == 0:
            q.append(i)
print(count)
