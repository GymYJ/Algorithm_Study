import sys
from collections import deque

n = int(sys.stdin.readline())
q = deque([])
size = 0
for _ in range(n):
    operation = sys.stdin.readline().split()
    if operation[0] == 'push':
        q.append(operation[1])
        size += 1
    elif operation[0] == 'pop':
        if size == 0:
            print(-1)
        else:
            print(q.popleft())
            size -= 1
    elif operation[0] == 'size':
        print(size)
    elif operation[0] == 'empty':
        if size == 0:
            print(1)
        else:
            print(0)
    elif operation[0] == 'front':
        if size == 0:
            print(-1)
        else:
            print(q[0])
    elif operation[0] == 'back':
        if size == 0:
            print(-1)
        else:
            print(q[-1])
