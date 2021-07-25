import sys

n, k = map(int, sys.stdin.readline().split())
num = sys.stdin.readline().strip()
stack = []
size = 0
remove = 0
for s in num:
    if size == 0:
        stack.append(s)
        size += 1
    else:
        while remove < k and size != 0 and stack[-1] < s:
            stack.pop()
            size -= 1
            remove += 1
        stack.append(s)
        size += 1
if remove == k:
    print(''.join(stack))
else:
    print(''.join(stack[:-(k - remove)]))
