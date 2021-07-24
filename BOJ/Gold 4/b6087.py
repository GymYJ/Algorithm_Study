import sys
from collections import deque
from math import inf

w, h = map(int, sys.stdin.readline().split())
visit = [[[inf] * 2 for _ in range(w)] for _ in range(h)]
arr = []
C = []
for i in range(h):
    temp = list(sys.stdin.readline())
    for j in range(w):
        if temp[j] == 'C':
            C.append([i, j])
    arr.append(temp)
move = [[-1, 0], [1, 0], [0, -1], [0, 1]]
start = []
for m in move:
    start.append(C[0] + m + [0])
end = C[1]
visit[C[0][0]][C[0][1]][0] = 0
visit[C[0][0]][C[0][1]][1] = 0
q = deque(start)
answer = sys.maxsize
while q:
    x, y, mx, my, count = q.popleft()
    if count > answer:
        continue
    if x == end[0] and y == end[1]:
        if answer > count:
            answer = count
        continue
    for dx, dy in move:
        nx, ny = x + dx, y + dy
        c = 0
        d = 0
        if abs(mx - dx) == 1 and abs(my - dy) == 1:
            c = 1
        if dy == 0:
            d = 1
        if 0 <= nx < h and 0 <= ny < w and arr[nx][ny] != '*' and visit[nx][ny][d] > count + c:
            visit[nx][ny][d] = count + c
            q.append([nx, ny, dx, dy, count + c])
print(answer)
