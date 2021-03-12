import sys


s = set()
n = int(sys.stdin.readline())
for _ in range(n):
    op = sys.stdin.readline().strip().split()
    if op[0] == 'all':
        s = set([i for i in range(1, 21)])
    elif op[0] == 'empty':
        s = set()
    else:
        if op[0] == 'add':
            s.add(int(op[1]))
        elif op[0] == 'remove':
            s.discard(int(op[1]))
        elif op[0] == 'check':
            if int(op[1]) in s:
                print(1)
            else:
                print(0)
        else:
            if int(op[1]) in s:
                s.discard(int(op[1]))
            else:
                s.add(int(op[1]))
