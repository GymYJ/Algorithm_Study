# 분리 집합으로 풀어도 됨
import sys


def dfs(x, y, num):
    global n, m, arr, visit
    if visit[x][y] != 0:
        return visit[x][y]
    visit[x][y] = num
    if arr[x][y] == 'U':
        visit[x][y] = dfs(x - 1, y, num)
    elif arr[x][y] == 'D':
        visit[x][y] = dfs(x + 1, y, num)
    elif arr[x][y] == 'L':
        visit[x][y] = dfs(x, y - 1, num)
    elif arr[x][y] == 'R':
        visit[x][y] = dfs(x, y + 1, num)
    return visit[x][y]


n, m = map(int, sys.stdin.readline().split())
arr = []
for _ in range(n):
    arr.append(list(sys.stdin.readline().strip()))
visit = [[0 for _ in range(m)] for _ in range(n)]

move = [[-1, 0], [1, 0], [0, -1], [0, 1]]
temp = 1
for i in range(n):
    for j in range(m):
        if visit[i][j] == 0:
            dfs(i, j, temp)
            temp += 1
answer = set()
for v in visit:
    answer = answer.union(set(v))
print(len(answer))
