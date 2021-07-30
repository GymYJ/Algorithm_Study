import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
arr = []
red = []
blue = []
for i in range(n):
    temp = list(sys.stdin.readline().strip())
    arr.append(temp)
    for j in range(m):
        if temp[j] == 'R':
            red = [i, j]
        elif temp[j] == 'B':
            blue = [i, j]
q = deque([red + blue + [0]])
visit = [[[[0 for _ in range(m)] for _ in range(n)] for _ in range(m)] for _ in range(n)]
visit[red[0]][red[1]][blue[0]][blue[1]] = 1
answer = 0
move = [[-1, 0], [1, 0], [0, -1], [0, 1]]
while q:
    rx, ry, bx, by, count = q.popleft()
    if count >= 10:
        continue
    for dx, dy in move:
        r_goal = False
        b_goal = False
        nrx, nry = rx, ry
        while True:
            nrx, nry = nrx + dx, nry + dy
            if 0 <= nrx < n and 0 <= nry < m and arr[nrx][nry] != '#' and [nrx, nry] != [bx, by]:
                if arr[nrx][nry] == 'O':
                    r_goal = True
                    nrx, nry = -1, -1
                    break
                continue
            else:
                nrx, nry = nrx - dx, nry - dy
                break
        nbx, nby = bx, by
        while True:
            nbx, nby = nbx + dx, nby + dy
            if 0 <= nbx < n and 0 <= nby < m and arr[nbx][nby] != '#' and [nbx, nby] != [nrx, nry]:
                if arr[nbx][nby] == 'O':
                    b_goal = True
                    nbx, nby = -1, -1
                    break
                continue
            else:
                nbx, nby = nbx - dx, nby - dy
                break
        if not r_goal:
            while True:
                nrx, nry = nrx + dx, nry + dy
                if 0 <= nrx < n and 0 <= nry < m and arr[nrx][nry] != '#' and [nrx, nry] != [nbx, nby]:
                    if arr[nrx][nry] == 'O':
                        r_goal = True
                        nrx, nry = -1, -1
                        break
                    continue
                else:
                    nrx, nry = nrx - dx, nry - dy
                    break
        if r_goal and not b_goal:
            answer = 1
            break
        elif b_goal:
            continue
        if visit[nrx][nry][nbx][nby] == 0:
            visit[nrx][nry][nbx][nby] = 1
            q.append([nrx, nry, nbx, nby, count + 1])
    if answer == 1:
        break
print(answer)
