import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
arr = []
red = []
blue = []
hole = []
for i in range(n):
    temp = list(sys.stdin.readline().strip())
    for j in range(m):
        if temp[j] == 'R':
            red = [i, j]
        elif temp[j] == 'B':
            blue = [i, j]
        elif temp[j] == 'O':
            hole = [i, j]
    arr.append(temp)
move = [[-1, 0], [1, 0], [0, -1], [0, 1]]
visit = [[[[0 for _ in range(m)] for _ in range(n)] for _ in range(m)] for _ in range(n)]
visit[red[0]][red[1]][blue[0]][blue[1]] = 1
q = deque([[red, blue, 0]])
answer = -1
while q:
    r, b, count = q.popleft()
    for dx, dy in move:
        goal = []
        loc = [[r[0], r[1]], [b[0], b[1]]]
        seq = [[r, 'red'], [b, 'blue']]
        if dx == -1 and dy == 0 and r[1] == b[1] and r[0] > b[0]:
            seq = [[b, 'blue'], [r, 'red']]
        elif dx == 1 and dy == 0 and r[1] == b[1] and r[0] < b[0]:
            seq = [[b, 'blue'], [r, 'red']]
        elif dx == 0 and dy == -1 and r[0] == b[0] and r[1] > b[1]:
            seq = [[b, 'blue'], [r, 'red']]
        elif dx == 0 and dy == 1 and r[0] == b[0] and r[1] < b[1]:
            seq = [[b, 'blue'], [r, 'red']]
        for a, color in seq:
            x, y = a
            is_goal = False
            while True:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] != '#' and [nx, ny] not in loc:
                    if arr[nx][ny] == 'O':
                        is_goal = True
                        break
                    x, y = nx, ny
                else:
                    break
            if is_goal:
                goal.append(color)
                if color == 'red':
                    loc[0] = [-1, -1]
                else:
                    loc[1] = [-1, -1]
            else:
                if color == 'red':
                    loc[0] = [x, y]
                else:
                    loc[1] = [x, y]
        if 'red' in goal and 'blue' in goal:
            continue
        elif 'blue' in goal:
            continue
        elif 'red' in goal:
            answer = count + 1
            break
        else:
            if visit[loc[0][0]][loc[0][1]][loc[1][0]][loc[1][1]] != 1 and count < 9:
                visit[loc[0][0]][loc[0][1]][loc[1][0]][loc[1][1]] = 1
                q.append([loc[0], loc[1], count + 1])
    if answer != -1:
        break
print(answer)
