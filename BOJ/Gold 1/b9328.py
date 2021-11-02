import sys
from collections import deque


def select_type(i, j, q):
    global arr, answer, keys, doors
    if 'A' <= arr[i][j] <= 'Z':
        if arr[i][j] in keys:
            q.append([i, j])
        else:
            doors[arr[i][j]].append([i, j])
    elif 'a' <= arr[i][j] <= 'z':
        q.append([i, j])
        key = arr[i][j].upper()
        keys.add(key)
        while doors[key]:
            x, y = doors[key].pop()
            q.append([x, y])
    elif arr[i][j] == '$':
        answer += 1
        q.append([i, j])
    else:
        q.append([i, j])
    return q


def search(i, j):
    global arr, answer, h, w, keys, doors, visit
    q = deque()
    visit[i][j] = 1
    q = select_type(i, j, q)
    while q:
        x, y = q.popleft()
        for dx, dy in move:
            nx, ny = x + dx, y + dy
            if 0 <= nx < h and 0 <= ny < w and arr[nx][ny] != '*' and visit[nx][ny] == 0:
                visit[nx][ny] = 1
                q = select_type(nx, ny, q)


move = [[-1, 0], [1, 0], [0, -1], [0, 1]]
t = int(sys.stdin.readline())
for _ in range(t):
    h, w = map(int, sys.stdin.readline().split())
    arr = []
    for _ in range(h):
        arr.append(list(sys.stdin.readline().strip()))
    keys = sys.stdin.readline().strip()
    if keys == '0':
        keys = set()
    else:
        keys = set(list(keys.upper()))
    doors = {chr(i): [] for i in range(65, 91)}
    answer = 0
    visit = [[0 for _ in range(w)] for _ in range(h)]
    for i in [0, h - 1]:
        for j in range(w):
            if arr[i][j] != '*' and visit[i][j] == 0:
                search(i, j)
    for i in range(1, h - 1):
        for j in [0, w - 1]:
            if arr[i][j] != '*' and visit[i][j] == 0:
                search(i, j)
    check = True
    while check:
        check = False
        for key in keys:
            while doors[key]:
                check = True
                i, j = doors[key].pop()
                search(i, j)
    print(answer)
