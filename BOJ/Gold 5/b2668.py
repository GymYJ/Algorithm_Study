import sys


def dfs(now, first, second):
    global arr, ans, ans_list
    if visit[now] == 1:
        if sorted(first) == sorted(second):
            ans_list.append(first)
            return True
    else:
        visit[now] = 1
        if dfs(arr[now], first + [now], second + [arr[now]]):
            return True
        visit[now] = 0
    return False


n = int(sys.stdin.readline())
arr = [0]
for i in range(1, n + 1):
    num = int(sys.stdin.readline())
    arr.append(num)
ans = 0
ans_list = []
visit = [0 for _ in range(n + 1)]
for i in range(1, n + 1):
    if visit[i] == 0:
        visit[i] = 1
        dfs(arr[i], [i], [arr[i]])
temp = []
for a in ans_list:
    temp += a
temp.sort()
print(len(temp))
for i in temp:
    print(i)
