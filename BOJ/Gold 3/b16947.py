import sys

sys.setrecursionlimit(10000)


def find_circle(now, before, now_arr):
    global graph, visit
    for i in graph[now]:
        if visit[i] == 1 and i != before:
            return now_arr[now_arr.index(i):]
        if visit[i] == 0:
            visit[i] = 1
            result = find_circle(i, now, now_arr + [i])
            if result:
                return result
            visit[i] = 0
    return False


def dfs(now, before):
    global graph, answer
    if answer[now] == 0:
        return 1
    for i in graph[now]:
        if i != before:
            result = dfs(i, now)
            if result:
                answer[now] = result
                return result + 1
    return 0


n = int(sys.stdin.readline())
graph = {i: [] for i in range(1, n + 1)}
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
circle = []
visit = [0 for _ in range(n + 1)]
visit[1] = 1
circle += find_circle(1, 0, [1])
answer = [-1 for _ in range(n + 1)]
visit = [0 for _ in range(n + 1)]
for i in circle:
    answer[i] = 0
    visit[i] = 1
for i in range(1, n + 1):
    if answer[i] == -1:
        dfs(i, 0)
print(*answer[1:])
