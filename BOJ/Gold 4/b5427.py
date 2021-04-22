import sys
from collections import deque

t = int(sys.stdin.readline())
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for _ in range(t):
    w, h = map(int, sys.stdin.readline().split())
    arr = []
    sangun = deque([])
    visit = [[0 for _ in range(w)] for _ in range(h)]
    fire = deque([])
    fire_visit = [[0 for _ in range(w)] for _ in range(h)]
    for i in range(h):
        temp = list(sys.stdin.readline().strip())
        for j, s in enumerate(temp):
            if s == '@':
                sangun.append((i, j, 0))
                visit[i][j] = 1
            elif s == '*':
                fire.append((i, j))
                fire_visit[i][j] = 1
        arr.append(temp)
    answer = 0
    possible = False
    while sangun:
        new_fire = deque([])
        while fire:
            x, y = fire.popleft()
            for dx, dy in move:
                nx, ny = x + dx, y + dy
                if 0 <= nx < h and 0 <= ny < w and fire_visit[nx][ny] == 0 and arr[nx][ny] != '#':
                    fire_visit[nx][ny] = 1
                    new_fire.append((nx, ny))
        fire = new_fire
        new_sangun = deque([])
        while sangun:
            x, y, time = sangun.popleft()
            if x == 0 or x == h - 1 or y == 0 or y == w - 1:
                possible = True
                answer = time + 1
                break
            for dx, dy in move:
                nx, ny = x + dx, y + dy
                if 0 <= nx < h and 0 <= ny < w and fire_visit[nx][ny] == 0 and visit[nx][ny] == 0 and arr[nx][ny] != '#':
                    visit[nx][ny] = 1
                    new_sangun.append((nx, ny, time + 1))
        sangun = new_sangun
        if possible:
            break
    if possible:
        print(answer)
    else:
        print('IMPOSSIBLE')
