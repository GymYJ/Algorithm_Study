import sys

n = int(sys.stdin.readline())
answer = 0
stack = []
for _ in range(n):
    now = int(sys.stdin.readline())
    while stack and stack[-1] <= now:
        stack.pop()
    stack.append(now)
    answer += len(stack) - 1
print(answer)
