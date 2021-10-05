import sys
from copy import deepcopy


def dfs(x, y, num, now):
    global move, answer
    num += now[x][y][0]
    d = now[x][y][1]
    now[x][y] = []
    for k in range(1, 17):
        is_move = False
        for i in range(4):
            for j in range(4):
                if now[i][j] and now[i][j][0] == k:
                    is_move = True
                    fx, fy = i, j
                    move_num = now[i][j][1]
                    for _ in range(8):
                        dx, dy = move[move_num]
                        nx, ny = fx + dx, fy + dy
                        if 0 <= nx < 4 and 0 <= ny < 4 and not (nx == x and ny == y):
                            temp = [k, move_num]
                            now[i][j] = now[nx][ny]
                            now[nx][ny] = temp
                            break
                        move_num += 1
                        if move_num > 8:
                            move_num = 1
                    break
            if is_move:
                break
    shark_move = False
    for i in range(1, 4):
        dx, dy = move[d]
        nx, ny = x + dx * i, y + dy * i
        if 0 <= nx < 4 and 0 <= ny < 4 and now[nx][ny]:
            shark_move = True
            cp_now = deepcopy(now)
            dfs(nx, ny, num, cp_now)
    if not shark_move:
        answer = max(answer, num)


arr = []
for _ in range(4):
    temp = list(map(int, sys.stdin.readline().split()))
    row = []
    for i in range(0, 8, 2):
        row.append([temp[i], temp[i + 1]])
    arr.append(row)
move = [[0, 0], [-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1]]
answer = 0
dfs(0, 0, 0, arr)
print(answer)
