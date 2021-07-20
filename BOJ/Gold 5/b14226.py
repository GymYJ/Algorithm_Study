import sys
from collections import deque

s = int(sys.stdin.readline())
visit = [[0 for _ in range(1001)] for _ in range(1001)]
visit[1][0] = 1
q = deque([[1, 0, 0]])
answer = 0
while q:
    screen, clip, time = q.popleft()
    if screen == s:
        answer = time
        break
    if screen <= 1000 and visit[screen][screen] == 0:
        visit[screen][screen] = 1
        q.append([screen, screen, time + 1])
    if clip != 0 and screen + clip <= 1000 and visit[screen + clip][clip] == 0:
        visit[screen + clip][clip] = 1
        q.append([screen + clip, clip, time + 1])
    if screen > 0 and visit[screen - 1][clip] == 0:
        visit[screen - 1][clip] = 1
        q.append([screen - 1, clip, time + 1])
print(answer)
