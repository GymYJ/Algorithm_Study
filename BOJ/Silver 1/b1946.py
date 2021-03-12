import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, sys.stdin.readline().split())))
    arr.sort(reverse=True)
    count = 1
    min_y = arr.pop()[1]
    for _ in range(n // 2):
        now = arr.pop()
        if now[1] > min_y:
            continue
        min_y = now[1]
        count += 1
    arr.sort(reverse=True, key=lambda x: x[1])
    min_x = 100000
    while arr:
        now = arr.pop()
        if now[1] > min_y:
            break
        can = True
        if now[0] > min_x:
            continue
        min_x = now[0]
        count += 1
    print(count)
