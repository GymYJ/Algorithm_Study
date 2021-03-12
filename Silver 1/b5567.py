import sys
from collections import deque

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
dic = {i: [] for i in range(1, n + 1)}
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    dic[a].append(b)
    dic[b].append(a)
q = deque(dic[1])
visit = [1] + dic[1]
friends = len(dic[1])
answer = 0
while q:
    now = q.popleft()
    answer += 1
    if answer <= friends:
        for i in dic[now]:
            if i not in visit:
                q.append(i)
                visit.append(i)
print(answer)
