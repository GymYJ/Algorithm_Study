import sys


def dfs(now_arr, now_level):
    global level
    if len(now_arr) == 0:
        return
    mid = len(now_arr) // 2
    level[now_level].append(now_arr[mid])
    dfs(now_arr[:mid], now_level + 1)
    dfs(now_arr[mid + 1:], now_level + 1)


k = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
level = [[] for _ in range(11)]
dfs(arr, 1)
for i in range(1, k + 1):
    print(*level[i])
