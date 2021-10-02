import sys

n, k = map(int, sys.stdin.readline().split())
arr = [[-1 for _ in range(n + 1)]]
for _ in range(n):
    arr.append([-1] + list(map(int, sys.stdin.readline().split())))
stack = [[[] for _ in range(n + 1)] for _ in range(n + 1)]
move = [[0, 0], [0, 1], [0, - 1], [-1, 0], [1, 0]]
loc = {}
direct = {}
for i in range(1, k + 1):
    a, b, m = map(int, sys.stdin.readline().split())
    loc[i] = [a, b]
    direct[i] = move[m]
    stack[a][b] = [i]
answer = -1
for count in range(1, 1001):
    is_end = False
    for i in range(1, k + 1):
        x, y = loc[i]
        dx, dy = direct[i]
        nx, ny = x + dx, y + dy
        if nx <= 0 or nx > n or ny <= 0 or ny > n or arr[nx][ny] == 2:
            dx, dy = -1 * dx, -1 * dy
            direct[i] = [dx, dy]
            nx, ny = x + dx, y + dy
        if 0 < nx <= n and 0 < ny <= n:
            if arr[nx][ny] == 0:
                idx = stack[x][y].index(i)
                to_hold = stack[x][y][:idx]
                to_move = stack[x][y][idx:]
                stack[x][y] = to_hold
                stack[nx][ny] += to_move
                for j in to_move:
                    loc[j] = [nx, ny]
                if len(stack[nx][ny]) >= 4:
                    is_end = True
            elif arr[nx][ny] == 1:
                idx = stack[x][y].index(i)
                to_hold = stack[x][y][:idx]
                to_move = stack[x][y][idx:]
                stack[x][y] = to_hold
                to_move.reverse()
                stack[nx][ny] += to_move
                for j in to_move:
                    loc[j] = [nx, ny]
                if len(stack[nx][ny]) >= 4:
                    is_end = True
            else:
                continue

    if is_end:
        answer = count
        break
print(answer)
