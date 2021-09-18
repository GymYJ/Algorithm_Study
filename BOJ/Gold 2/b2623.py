import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
seq = {i: [] for i in range(1, n + 1)}
degree = {i: 0 for i in range(1, n + 1)}
for _ in range(m):
    singer = list(map(int, sys.stdin.readline().split()))
    before = singer[1]
    for num in singer[2:]:
        seq[before].append(num)
        degree[num] += 1
        before = num
q = deque()
for i in range(1, n + 1):
    if degree[i] == 0:
        q.append(i)
answer = []
while q:
    now = q.popleft()
    answer.append(now)
    for num in seq[now]:
        degree[num] -= 1
        if degree[num] == 0:
            q.append(num)
if len(answer) == n:
    for num in answer:
        print(num)
else:
    print(0)
