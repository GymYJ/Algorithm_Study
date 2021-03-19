import sys

r, c = map(int, sys.stdin.readline().split())
arr = []
for _ in range(r):
    arr.append(list(sys.stdin.readline().strip()))
answer = 0
alpha = [0 for _ in range(26)]


def dfs(x, y, count):
    global answer, r, c, arr, alpha
    move = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    end = True
    for dx, dy in move:
        nx, ny = x + dx, y + dy
        if 0 <= nx < r and 0 <= ny < c and alpha[ord(str(arr[nx][ny])) - 65] == 0:
            alpha[ord(str(arr[nx][ny])) - 65] = 1
            dfs(nx, ny, count + 1)
            alpha[ord(str(arr[nx][ny])) - 65] = 0
            end = False
    if end and answer < count:
        answer = count


alpha[ord(str(arr[0][0])) - 65] = 1
dfs(0, 0, 1)
print(answer)
