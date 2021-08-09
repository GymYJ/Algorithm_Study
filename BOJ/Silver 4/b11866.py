import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
q = deque([i for i in range(1, n + 1)])
size = n
print('<', end='')
count = 0
while size > 1:
    now = q.popleft()
    count += 1
    if count == k:
        print(f'{now},', end=' ')
        size -= 1
        count = 0
    else:
        q.append(now)
print(f'{q[0]}>')
