import sys
from collections import deque

m, n, k = map(int, sys.stdin.readline().split())
arr = [[0 for _ in range(n)] for _ in range(m)]
for _ in range(k):
    lx, ly, rx, ry = map(int, sys.stdin.readline().split())
    for i in range(ly, ry):
        for j in range(lx, rx):
            arr[i][j] = 1
count = 0
answer = []
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visit = []
for y in range(m):
    for x in range(n):
        if arr[y][x] == 0 and (x, y) not in visit:
            count += 1
            size = 1
            q = deque([(x, y)])
            visit.append((x, y))
            while q:
                n_x, n_y = q.popleft()
                for dx, dy in move:
                    next_x = n_x + dx
                    next_y = n_y + dy
                    if 0 <= next_x < n and 0 <= next_y < m and arr[next_y][next_x] == 0 and \
                            (next_x, next_y) not in visit:
                        q.append((next_x, next_y))
                        visit.append((next_x, next_y))
                        size += 1
            answer.append(size)
print(count)
answer.sort()
print(' '.join(list(map(str, answer))))
