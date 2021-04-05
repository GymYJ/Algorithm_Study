import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
s = [0 for _ in range(101)]
for _ in range(n + m):
    a, b = map(int, sys.stdin.readline().split())
    s[a] = b
visit = [0 for _ in range(101)]
q = deque([[1, 0]])
answer = sys.maxsize
while q:
    now, count = q.popleft()
    if answer < count:
        continue
    if now == 100:
        if answer > count:
            answer = count
        continue
    if s[now] != 0:
        next_ = s[now]
        if visit[next_] == 0 or visit[next_] > count:
            q.append([next_, count])
            visit[next_] = count
        continue
    for i in range(1, 7):
        next_ = now + i
        if next_ <= 100 and (visit[next_] == 0 or visit[next_] > count + 1):
            q.append([next_, count + 1])
            visit[next_] = count + 1
print(answer)
