import sys


def up_dfs(now):
    global students, visit
    for i in students[now]['up']:
        if visit[i] == 0:
            visit[i] = 1
            up_dfs(i)


def down_dfs(now):
    global students, visit
    for i in students[now]['down']:
        if visit[i] == 0:
            visit[i] = 1
            down_dfs(i)


n, m = map(int, sys.stdin.readline().split())
students = {i: {'up': [], 'down': []} for i in range(1, n + 1)}
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    students[a]['up'].append(b)
    students[b]['down'].append(a)

answer = 0
for i in range(1, n + 1):
    visit = [0] * (n + 1)
    visit[i] = 1
    up_dfs(i)
    down_dfs(i)
    if sum(visit) == n:
        answer += 1
print(answer)
