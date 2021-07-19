import sys


def dfs(now, i):
    global arr, n, s, answer
    if i == n:
        return
    now += arr[i]
    if now == s:
        answer += 1
    dfs(now - arr[i], i + 1)
    dfs(now, i + 1)


n, s = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
answer = 0
dfs(0, 0)
print(answer)
