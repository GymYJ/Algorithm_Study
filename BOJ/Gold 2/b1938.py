import sys
from collections import deque

n = int(sys.stdin.readline())
arr = []
start = []
end = []
for i in range(n):
    temp = list(sys.stdin.readline().strip())
    arr.append(temp)
    for j in range(n):
        if temp[j] == 'B':
            start.append((i, j))
        elif temp[j] == 'E':
            end.append((i, j))
visit = {tuple(start): 0}
if start[0][0] == start[1][0]:
    start.append(0)  # 가로
else:
    start.append(1)  # 세로
start.append(0)
answer = 0
q = deque([start])
move = [[-1, 0], [1, 0], [0, -1], [0, 1]]
while q:
    a, b, c, di, count = q.popleft()
    if [a, b, c] == end:
        answer = count
        break
    ax, ay = a
    bx, by = b
    cx, cy = c
    for dx, dy in move:
        nax, nay = ax + dx, ay + dy
        nbx, nby = bx + dx, by + dy
        ncx, ncy = cx + dx, cy + dy
        next_B = [(nax, nay), (nbx, nby), (ncx, ncy)]
        if (0 <= nax < n and 0 <= nay < n and arr[nax][nay] != '1') and (
                0 <= nbx < n and 0 <= nby < n and arr[nbx][nby] != '1') and (
                0 <= ncx < n and 0 <= ncy < n and arr[ncx][ncy] != '1') and (
                not visit.get(tuple(next_B)) or visit[tuple(next_B)] > count + 1):
            visit[tuple(next_B)] = count + 1
            next_B.append(di)
            next_B.append(count + 1)
            q.append(next_B)
    if di == 0:
        temp = [(ax - 1, ay), (ax + 1, ay), (bx - 1, by), (bx + 1, by), (cx - 1, cy), (cx + 1, cy)]
        check = True
        for x, y in temp:
            if 0 <= x < n and 0 <= y < n and arr[x][y] != '1':
                continue
            else:
                check = False
                break
        if check:
            next_B = [(bx - 1, by), (bx, by), (bx + 1, by)]
            if not visit.get(tuple(next_B)) or visit[tuple(next_B)] > count + 1:
                visit[tuple(next_B)] = count + 1
                next_B.append(1)
                next_B.append(count + 1)
                q.append(next_B)
    else:
        temp = [(ax, ay - 1), (ax, ay + 1), (bx, by - 1), (bx, by + 1), (cx, cy - 1), (cx, cy + 1)]
        check = True
        for x, y in temp:
            if 0 <= x < n and 0 <= y < n and arr[x][y] != '1':
                continue
            else:
                check = False
                break
        if check:
            next_B = [(bx, by - 1), (bx, by), (bx, by + 1)]
            if not visit.get(tuple(next_B)) or visit[tuple(next_B)] > count + 1:
                visit[tuple(next_B)] = count + 1
                next_B.append(0)
                next_B.append(count + 1)
                q.append(next_B)

print(answer)
