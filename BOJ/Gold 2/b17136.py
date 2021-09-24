import sys


def dfs(x, y, use):
    global arr, paper, answer
    if use >= answer:
        return
    if y >= 10:
        answer = min(answer, use)
        return
    if x >= 10:
        dfs(0, y + 1, use)
        return
    if arr[x][y] == 1:
        for s in range(1, 6):
            if paper[s] == 0:
                continue
            if x + s > 10 or y + s > 10:
                continue

            is_p = True
            for i in range(x, x + s):
                for j in range(y, y + s):
                    if arr[i][j] == 0:
                        is_p = False
                        break
                if not is_p:
                    break

            if is_p:
                for i in range(x, x + s):
                    for j in range(y, y + s):
                        arr[i][j] = 0
                paper[s] -= 1
                dfs(x + s, y, use + 1)
                paper[s] += 1
                for i in range(x, x + s):
                    for j in range(y, y + s):
                        arr[i][j] = 1
    else:
        dfs(x + 1, y, use)


arr = []
for _ in range(10):
    arr.append(list(map(int, sys.stdin.readline().split())))
visit = [[0 for _ in range(10)] for _ in range(10)]
paper = [0, 5, 5, 5, 5, 5]
answer = 26
dfs(0, 0, 0)
if answer != 26:
    print(answer)
else:
    print(-1)
