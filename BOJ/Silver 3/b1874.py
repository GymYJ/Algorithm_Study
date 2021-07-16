import sys

n = int(sys.stdin.readline())
arr = []
stack = []
answer = []
num = 1
is_p = True
for _ in range(n):
    now = int(sys.stdin.readline())
    while is_p:
        if num > n + 1:
            is_p = False
            break
        if len(stack) == 0 or stack[-1] < now:
            answer.append('+')
            stack.append(num)
            num += 1
        elif stack[-1] == now:
            answer.append('-')
            stack.pop()
            break
        else:
            is_p = False
            break
if is_p:
    for s in answer:
        print(s)
else:
    print('NO')
