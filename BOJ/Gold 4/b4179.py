import sys
from collections import deque

r, c = map(int, sys.stdin.readline().split())
arr = []
jihoon = []
fire = []
for i in range(r):
    temp = list(sys.stdin.readline().strip())
    arr.append(temp)
    if 'J' in temp:
        jihoon = [i, temp.index("J"), 0]
    for j, s in enumerate(temp):
        if s == 'F':
            fire.append([i, j])

visit = [[0 for _ in range(c)] for _ in range(r)]
visit[jihoon[0]][jihoon[1]] = 1
is_p = False
answer = 0
jq = deque([jihoon])
fq = deque(fire)
move = [[-1, 0], [1, 0], [0, -1], [0, 1]]
while jq:
    new_fq = deque()
    while fq:
        x, y = fq.popleft()
        for dx, dy in move:
            nx, ny = x + dx, y + dy
            if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] != '#' and arr[nx][ny] != 'F':
                arr[nx][ny] = 'F'
                new_fq.append([nx, ny])
    fq = new_fq
    new_jq = deque()
    while jq:
        x, y, count = jq.popleft()
        for dx, dy in move:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                is_p = True
                answer = count + 1
                break
            if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] == '.' and visit[nx][ny] == 0:
                visit[nx][ny] = 1
                new_jq.append([nx, ny, count + 1])
        if is_p:
            break
    if is_p:
        break
    jq = new_jq
print(answer if is_p else 'IMPOSSIBLE')
