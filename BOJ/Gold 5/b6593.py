import sys
from collections import deque

move = [[-1, 0, 0], [1, 0, 0], [0, -1, 0], [0, 1, 0], [0, 0, -1], [0, 0, 1]]
while True:
    L, R, C = map(int, sys.stdin.readline().split())
    if L == 0:
        break
    arr = []
    start = [0, 0, 0]
    visit = [[[0 for _ in range(C)] for _ in range(R)] for _ in range(L)]
    for i in range(L):
        layer = []
        for j in range(R):
            temp = list(sys.stdin.readline().strip())
            if 'S' in temp:
                start = [i, j, temp.index('S')]
                visit[i][j][temp.index('S')] = 1
            layer.append(temp)
        arr.append(layer)
        sys.stdin.readline()

    answer = 0
    q = deque([start + [0]])
    while q:
        x, y, z, time = q.popleft()
        if arr[x][y][z] == 'E':
            answer = time
            break
        for dx, dy, dz in move:
            nx, ny, nz = x + dx, y + dy, z + dz
            if 0 <= nx < L and 0 <= ny < R and 0 <= nz < C and arr[nx][ny][nz] != '#' and visit[nx][ny][nz] == 0:
                visit[nx][ny][nz] = 1
                q.append([nx, ny, nz, time + 1])
    if answer != 0:
        print(f'Escaped in {answer} minute(s).')
    else:
        print('Trapped!')
