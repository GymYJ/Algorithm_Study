import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
answer = [-1]
stack = [arr.pop()]
size = 1
while arr:
    now = arr.pop()
    check = False
    while size > 0:
        if stack[-1] > now:
            answer.append(stack[-1])
            check = True
            break
        else:
            stack.pop()
            size -= 1
    if not check:
        answer.append(-1)
    stack.append(now)
    size += 1
answer.reverse()
print(' '.join(list(map(str, answer))))
