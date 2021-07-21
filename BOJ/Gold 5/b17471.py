import sys
from collections import deque
from math import inf


def check(now, visit):
    global n, dic
    q = deque([now])
    visit[now] = 1
    a_list = [now]
    while q:
        now = q.popleft()
        for i in dic[now]:
            if visit[i] == 0:
                visit[i] = 1
                a_list.append(i)
                q.append(i)
    total = sum(visit)
    for i in a_list:
        visit[i] = 0
    if total == n:
        return True
    return False


n = int(sys.stdin.readline())
arr = [0] + list(map(int, sys.stdin.readline().split()))
dic = {i: [] for i in range(1, n + 1)}
for i in range(1, n + 1):
    temp = list(map(int, sys.stdin.readline().split()))
    dic[i] = temp[1:]
visit = [0 for _ in range(n + 1)]
visit[1] = 1
answer = inf
q = deque([[1, arr[1], sum(arr) - arr[1], visit]])
while q:
    now, a, b, cp_visit = q.popleft()
    if answer > abs(a - b):
        other = 0
        for i in range(1, n + 1):
            if cp_visit[i] == 0:
                other = i
                break
        if check(other, cp_visit):
            answer = abs(a - b)
    else:
        continue
    for i in dic[now]:
        if cp_visit[i] == 0:
            cp = cp_visit.copy()
            cp[i] = 1
            q.append([i, a + arr[i], b - arr[i], cp])
print(answer if answer != inf else -1)
