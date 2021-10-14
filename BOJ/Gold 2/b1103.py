import sys


def dfs(x, y, count):
    global n, m, arr, visit, move, answer
    num = int(arr[x][y])
    for dx, dy in move:
        nx, ny = x + dx * num, y + dy * num
        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] != 'H':
            if visit[nx][ny] == 1:
                print(-1)
                exit()
            elif maxi[nx][ny] < count + 1:
                maxi[nx][ny] = count + 1
                visit[nx][ny] = 1
                dfs(nx, ny, count + 1)
                visit[nx][ny] = 0
        else:
            answer = max(answer, count + 1)


sys.setrecursionlimit(100000)
n, m = map(int, sys.stdin.readline().split())
arr = []
visit = [[0 for _ in range(m)] for _ in range(n)]
maxi = [[0 for _ in range(m)] for _ in range(n)]
move = [[-1, 0], [1, 0], [0, -1], [0, 1]]
answer = 0
for _ in range(n):
    arr.append(list(sys.stdin.readline().strip()))
visit[0][0] = 1
dfs(0, 0, 0)
print(answer)
