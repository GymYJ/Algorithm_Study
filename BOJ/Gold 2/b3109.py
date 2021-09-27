import sys


def dfs(x, y):
    global arr, visit, answer, move, r, c
    if y == c - 1:
        answer += 1
        return True
    for dx, dy in move:
        nx, ny = x + dx, y + dy
        if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] == '.' and visit[nx][ny] == 0:
            visit[nx][ny] = 1
            if dfs(nx, ny):
                return True
    return False


r, c = map(int, sys.stdin.readline().split())
arr = []
for _ in range(r):
    arr.append(list(sys.stdin.readline().strip()))
answer = 0
visit = [[0 for _ in range(c)] for _ in range(r)]
move = [[-1, 1], [0, 1], [1, 1]]
for i in range(r):
    dfs(i, 0)
print(answer)
