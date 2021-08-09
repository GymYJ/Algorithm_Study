import sys

t = int(sys.stdin.readline())
for _ in range(t):
    string = sys.stdin.readline().strip()
    stack = []
    size = 0
    is_p = True
    for s in string:
        if s == '(':
            stack.append(s)
            size += 1
        else:
            if size == 0:
                is_p = False
                break
            stack.pop()
            size -= 1
    if is_p and size == 0:
        print('YES')
    else:
        print('NO')
