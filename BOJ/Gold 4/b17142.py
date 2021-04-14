import sys
import copy
from itertools import combinations
from collections import deque
from math import inf

n, m = map(int, sys.stdin.readline().split())
arr = []
virus = []
area = 0
answer = inf
for i in range(n):
    read = list(map(int, sys.stdin.readline().split()))
    temp = []
    for j, num in enumerate(read):
        if num == 2:
            virus.append((i, j, 0))
            temp.append(-1)
        elif num == 1:
            temp.append(1)
        else:
            temp.append(0)
            area += 1
    arr.append(temp)
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
sec = inf
for v in combinations(virus, m):
    visit = copy.deepcopy(arr)
    for x, y, _ in list(v):
        visit[x][y] = 1
    q = deque(list(v))
    count = area
    if count == 0:
        answer = 0
        break
    while q:
        x, y, sec = q.popleft()
        if answer < sec:
            break
        for dx, dy in move:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                if visit[nx][ny] == 0:
                    count -= 1
                    visit[nx][ny] = 1
                    q.append((nx, ny, sec + 1))
                elif visit[nx][ny] == -1:
                    visit[nx][ny] = 1
                    q.append((nx, ny, sec + 1))
        if count == 0:
            sec += 1
            break
    if count == 0 and answer > sec:
        answer = sec
print(answer if answer != inf else -1)
