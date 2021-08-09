import sys

n = int(sys.stdin.readline())
stack = []
size = 0
for _ in range(n):
    operation = sys.stdin.readline().split()
    if operation[0] == 'push':
        stack.append(operation[1])
        size += 1
    elif operation[0] == 'pop':
        if size == 0:
            print(-1)
        else:
            print(stack.pop())
            size -= 1
    elif operation[0] == 'size':
        print(size)
    elif operation[0] == 'empty':
        if size == 0:
            print(1)
        else:
            print(0)
    elif operation[0] == 'top':
        if size == 0:
            print(-1)
        else:
            print(stack[-1])
