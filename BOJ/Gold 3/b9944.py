import sys


def dfs(x, y, dx, dy, count, stage):
    global n, m, arr, visit, void, answer
    if count == void:
        answer = min(answer, stage)
        return
    nx, ny = x + dx, y + dy
    if 0 <= nx < n and 0 <= ny < m and visit[nx][ny] == 0 and arr[nx][ny] == '.':
        visit[nx][ny] = 1
        dfs(nx, ny, dx, dy, count + 1, stage)
        visit[nx][ny] = 0
    else:
        for dx, dy in move:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and visit[nx][ny] == 0 and arr[nx][ny] == '.':
                visit[nx][ny] = 1
                dfs(nx, ny, dx, dy, count + 1, stage + 1)
                visit[nx][ny] = 0


q = 0
move = [[0, -1], [0, 1], [-1, 0], [1, 0]]
while True:
    try:
        q += 1
        n, m = map(int, input().split())
        arr = []
        void = 0
        for _ in range(n):
            temp = list(sys.stdin.readline().strip())
            void += temp.count('.')
            arr.append(temp)
        answer = 1000001
        if void == 1:
            print(f'Case {q}: 0')
            continue
        for i in range(n):
            for j in range(m):
                if arr[i][j] == '.':
                    visit = [[0 for _ in range(m)] for _ in range(n)]
                    visit[i][j] = 1
                    for dx, dy in move:
                        dfs(i, j, dx, dy, 1, 1)
                    visit[i][j] = 0
        if answer == 1000001:
            answer = -1
        print(f'Case {q}: {answer}')
    except EOFError:
        break
