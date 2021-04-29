import sys
from collections import deque

n, m, fuel = map(int, sys.stdin.readline().split())
arr = [[1 for _ in range(n + 1)]]
department = [[0, 0], [0, 0]]
for _ in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    arr.append([1] + temp)
taxi = list(map(int, sys.stdin.readline().split()))
for i in range(2, m + 2):
    a, b, c, d = map(int, sys.stdin.readline().split())
    arr[a][b] = i
    department.append([c, d])
move = [[-1, 0], [1, 0], [0, -1], [0, 1]]
while fuel > 0 and m > 0:
    q = deque([taxi + [0]])
    visit = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    visit[taxi[0]][taxi[1]] = 1
    find = False
    length = 0
    c_list = []
    while q:
        x, y, l = q.popleft()
        if l > fuel:
            break
        if arr[x][y] >= 2:
            if not find:
                find = True
                length = l
                c_list.append([x, y])
            else:
                if l == length:
                    c_list.append([x, y])
            continue
        for dx, dy in move:
            nx, ny = x + dx, y + dy
            if 0 < nx <= n and 0 < ny <= n and visit[nx][ny] == 0 and arr[nx][ny] != 1:
                visit[nx][ny] = 1
                q.append([nx, ny, l + 1])
    if not find:
        break
    c_list.sort()
    c = c_list[0]
    c_num = arr[c[0]][c[1]]
    arr[c[0]][c[1]] = 0
    fuel -= length
    if fuel < 1:
        break

    taxi = c
    q = deque([taxi + [0]])
    visit = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    visit[taxi[0]][taxi[1]] = 1
    find = False
    length = 0
    while q:
        x, y, l = q.popleft()
        if l > fuel:
            break
        if [x, y] == department[c_num]:
            taxi = [x, y]
            find = True
            length = l
            break
        for dx, dy in move:
            nx, ny = x + dx, y + dy
            if 0 < nx <= n and 0 < ny <= n and visit[nx][ny] == 0 and arr[nx][ny] != 1:
                visit[nx][ny] = 1
                q.append([nx, ny, l + 1])
    if not find:
        break
    fuel += length
    m -= 1
print(fuel if m == 0 else -1)
