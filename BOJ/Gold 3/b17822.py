import sys
from collections import deque

n, m, t = map(int, sys.stdin.readline().split())
arr = [[0 for _ in range(m)]]
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))
for _ in range(t):
    x, d, k = map(int, sys.stdin.readline().split())
    for i in range(x, n + 1, x):
        for _ in range(k):
            temp_arr = arr[i]
            if d == 0:
                temp = temp_arr[-1]
                for j in range(m - 2, -1, -1):
                    temp_arr[j + 1] = temp_arr[j]
                temp_arr[0] = temp
                arr[i] = temp_arr
            else:
                temp = temp_arr[0]
                for j in range(0, m - 1):
                    temp_arr[j] = temp_arr[j + 1]
                temp_arr[-1] = temp
                arr[i] = temp_arr
    erase = 0
    visit = [[0 for _ in range(m)] for _ in range(n + 1)]
    move = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    for i in range(1, n + 1):
        for j in range(m):
            if arr[i][j] != 0:
                find = 1
                q = deque([[i, j]])
                value = arr[i][j]
                arr[i][j] = 0
                while q:
                    x, y = q.popleft()
                    for dx, dy in move:
                        nx, ny = x + dx, y + dy
                        if ny == -1:
                            ny = m - 1
                        elif ny == m:
                            ny = 0
                        if 0 < nx <= n and arr[nx][ny] == value:
                            arr[nx][ny] = 0
                            find += 1
                            q.append([nx, ny])
                if find == 1:
                    arr[i][j] = value
                else:
                    erase += find
    if erase == 0:
        total = 0
        count = 0
        for i in range(1, n + 1):
            for j in range(m):
                if arr[i][j] != 0:
                    total += arr[i][j]
                    count += 1
        if count == 0:
            continue
        avg = total / count
        for i in range(1, n + 1):
            for j in range(m):
                if arr[i][j] != 0:
                    if arr[i][j] > avg:
                        arr[i][j] -= 1
                    elif arr[i][j] < avg:
                        arr[i][j] += 1
print(sum([sum(arr[i]) for i in range(1, n + 1)]))
