import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
if n == k:
    print(0)
    print(n)
    sys.exit()
visit = [0 for _ in range(100001)]
visit[n] = 1
q = deque([(n, 0)])
answer = 100000
dic = {}
ans_list = []
while q:
    now, time = q.popleft()
    if now == k:
        answer = time
        for _ in range(time):
            ans_list.append(now)
            now = dic[now]
        ans_list.append(now)
        ans_list.reverse()
        break
    for dx in [-1, 1, now]:
        nx = now + dx
        if 0 <= nx <= 100000 and visit[nx] == 0:
            visit[nx] = 1
            dic[nx] = now
            q.append((nx, time + 1))
print(answer)
print(' '.join(list(map(str, ans_list))))
