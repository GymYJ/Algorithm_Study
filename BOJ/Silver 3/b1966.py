import sys
from collections import deque

t = int(sys.stdin.readline())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    q = deque(arr)
    index = deque([i for i in range(n)])
    max_num = max(q)
    count = 1
    while True:
        if index[0] == m and q[0] == max_num:
            print(count)
            break
        else:
            if q[0] == max_num:
                q.popleft()
                index.popleft()
                max_num = max(q)
                count += 1
            else:
                q.append(q.popleft())
                index.append(index.popleft())
