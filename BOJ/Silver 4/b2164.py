import sys
from collections import deque

n = int(sys.stdin.readline())
arr = [i for i in range(1, n + 1)]
q = deque(arr)
while n > 1:
    q.popleft()
    n -= 1
    q.append(q.popleft())
print(q[0])
