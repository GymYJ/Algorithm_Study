import sys


def dfs(now, count):
    global dic, visit, answer
    if count == 5:
        return True
    for i in dic[now]:
        if visit[i] == 0:
            visit[i] = 1
            if dfs(i, count + 1):
                return True
            visit[i] = 0
    return False


n, m = map(int, sys.stdin.readline().split())
dic = {i: [] for i in range(n)}
visit = [0 for _ in range(n)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    dic[a].append(b)
    dic[b].append(a)
answer = 0
for i in range(n):
    visit[i] = 1
    if dfs(i, 1):
        answer = 1
        break
    visit[i] = 0
print(answer)
