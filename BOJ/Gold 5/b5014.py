import sys
from collections import deque

f, s, g, u, d = map(int, sys.stdin.readline().split())
visit = [0 for _ in range(f + 1)]
visit[s] = 1
q = deque([(s, 0)])
answer = sys.maxsize
find = False
while q:
    now, count = q.popleft()
    if answer < count:
        continue
    if now == g:
        if answer > count:
            answer = count
            find = True
        continue
    for move in [u, -d]:
        next_f = now + move
        if 1 <= next_f <= f and visit[next_f] == 0:
            q.append((next_f, count + 1))
            visit[next_f] = 1
if find:
    print(answer)
else:
    print("use the stairs")
