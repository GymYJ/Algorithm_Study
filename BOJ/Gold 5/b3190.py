import sys
from collections import deque

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
apple = []
for _ in range(k):
    apple.append(list(map(int, sys.stdin.readline().split())))
l = int(sys.stdin.readline())
move = []
for _ in range(l):
    x, c = sys.stdin.readline().split()
    move.append([int(x), c])
direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
now = 0
q = deque([[1, 1]])
answer = 0
over = False
for x, c in move:
    time = x - answer
    for _ in range(time):
        answer += 1
        go = [q[-1][0] + direction[now][0], q[-1][1] + direction[now][1]]
        if go in q or not (0 < go[0] <= n) or not (0 < go[1] <= n):
            over = True
            break
        q.append(go)
        if go in apple:
            apple.remove(go)
        else:
            q.popleft()
    if over:
        break
    if c == 'L':
        if now == 0:
            now = 3
        else:
            now -= 1
    else:
        if now == 3:
            now = 0
        else:
            now += 1
if over:
    print(answer)
else:
    while True:
        answer += 1
        go = [q[-1][0] + direction[now][0], q[-1][1] + direction[now][1]]
        if go in q or not (0 < go[0] <= n) or not (0 < go[1] <= n):
            break
        q.append(go)
        if go in apple:
            apple.remove(go)
        else:
            q.popleft()
    print(answer)
