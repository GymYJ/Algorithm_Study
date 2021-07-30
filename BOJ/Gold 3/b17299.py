import sys
from collections import defaultdict

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
count = defaultdict(int)
most = 0
for i in arr:
    count[i] += 1
    most = max(most, count[i])
ngf = [-1] * n
stack = []
size = 0
for i in range(n - 1, -1, -1):
    if size == 0:
        stack.append((arr[i], count[arr[i]]))
        size += 1
    else:
        find = -1
        while stack:
            if stack[-1][1] > count[arr[i]]:
                find = stack[-1][0]
                break
            stack.pop()
            size -= 1
        ngf[i] = find
        stack.append((arr[i], count[arr[i]]))
        size += 1
print(*ngf)
