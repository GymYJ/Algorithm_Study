import sys
from collections import deque

n = int(sys.stdin.readline())
answer = 10000000
a_list = []
visit = [0 for _ in range(n + 1)]
visit[n] = 1
q = deque([(n, [n], 0)])
while q:
    now, n_list, count = q.popleft()
    if now == 1:
        answer = count
        a_list = n_list
        break
    if now % 3 == 0 and visit[now // 3] == 0:
        visit[now // 3] = 1
        q.append((now // 3, n_list + [now // 3], count + 1))
    if now % 2 == 0 and visit[now // 2] == 0:
        visit[now // 2] = 1
        q.append((now // 2, n_list + [now // 2], count + 1))
    if visit[now - 1] == 0:
        visit[now - 1] = 1
        q.append((now - 1, n_list + [now - 1], count + 1))
print(answer)
print(' '.join(list(map(str, a_list))))
