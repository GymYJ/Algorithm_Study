import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.reverse()
answer = [0 for _ in range(n)]
stack = [(arr[0], 0)]
for i, num in enumerate(arr[1:], start=1):
    if not stack:
        stack.append((num, i))
    if num < stack[-1][0]:
        stack.append((num, i))
    else:
        while stack:
            if num >= stack[-1][0]:
                _, idx = stack.pop()
                answer[n - idx - 1] = n - i
            else:
                break
        stack.append((num, i))
print(' '.join(list(map(str, answer))))
