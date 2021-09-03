import sys

n, m, k = map(int, sys.stdin.readline().split())
arr = []
now_space = [[-1, -1] for _ in range(m + 1)]
for i in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    for j in range(n):
        if temp[j] != 0:
            now_space[temp[j]] = [i, j]
    arr.append(temp)
now_direction = [0] + list(map(int, sys.stdin.readline().split()))
priority = [[]]
for i in range(m):
    temp = [[0, 0, 0, 0]]
    for _ in range(4):
        temp.append(list(map(int, sys.stdin.readline().split())))
    priority.append(temp)
move = [[0, 0], [-1, 0], [1, 0], [0, -1], [0, 1]]
smell_map = [[[0, 0] for _ in range(n)] for _ in range(n)]
for i in range(1, m + 1):
    x, y = now_space[i]
    smell_map[x][y] = [i, k]
answer = 0
shark = m
while shark > 1 and answer <= 1000:
    for i in range(1, m + 1):
        x, y = now_space[i]
        if x == -1 and y == -1:
            continue
        can_move = False
        for num in priority[i][now_direction[i]]:
            dx, dy = move[num]
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and smell_map[nx][ny] == [0, 0]:
                can_move = True
                arr[x][y] = 0
                now_space[i] = [nx, ny]
                now_direction[i] = num
                break
        if not can_move:
            for num in priority[i][now_direction[i]]:
                dx, dy = move[num]
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and smell_map[nx][ny][0] == i:
                    arr[x][y] = 0
                    now_space[i] = [nx, ny]
                    now_direction[i] = num
                    break
    for x in range(n):
        for y in range(n):
            if smell_map[x][y][0] != 0:
                smell_map[x][y][1] -= 1
                if smell_map[x][y][1] == 0:
                    smell_map[x][y] = [0, 0]
    for i in range(1, m + 1):
        x, y = now_space[i]
        if x == -1 and y == -1:
            continue
        if arr[x][y] == 0:
            arr[x][y] = i
            smell_map[x][y] = [i, k]
        elif arr[x][y] < i:
            shark -= 1
            now_space[i] = [-1, -1]
    answer += 1

print(answer if answer <= 1000 else -1)
