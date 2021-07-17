import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    arr.sort()
    top = arr.pop()
    left = arr.pop()
    right = arr.pop()
    level = max(top - left, top - right)
    while arr:
        now = arr.pop()
        if left > right:
            level = max(level, left - now)
            left = now
        else:
            level = max(level, right - now)
            right = now
    level = max(level, abs(left - right))
    print(level)
