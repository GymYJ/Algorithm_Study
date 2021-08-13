import sys
from collections import deque

r, c = map(int, sys.stdin.readline().split())
arr = []
mos = []
zag = []
for i in range(r):
    temp = list(sys.stdin.readline().strip())
    for j in range(c):
        if temp[j] == 'M':
            mos = [i, j]
        elif temp[j] == 'Z':
            zag = [i, j]
    arr.append(temp)
move = [[-1, 0], [1, 0], [0, -1], [0, 1]]
for temp in [mos, zag]:
    start = []
    for dx, dy in move:
        nx, ny = temp[0] + dx, temp[1] + dy
        if 0 <= nx < r and 0 <= ny < c:
            if [dx, dy] == [-1, 0] and (arr[nx][ny] in ['|', '+', '1', '4']):
                start = temp + [dx, dy]
                break
            elif [dx, dy] == [1, 0] and (arr[nx][ny] in ['|', '+', '2', '3']):
                start = temp + [dx, dy]
                break
            elif [dx, dy] == [0, -1] and (arr[nx][ny] in ['-', '+', '1', '2']):
                start = temp + [dx, dy]
                break
            elif [dx, dy] == [0, 1] and (arr[nx][ny] in ['-', '+', '3', '4']):
                start = temp + [dx, dy]
                break
    if start:
        break
q = deque([start])
blank = []
while q:
    x, y, dx, dy = q.popleft()
    nx, ny = x + dx, y + dy
    if arr[nx][ny] == '1':
        if [dx, dy] == [-1, 0]:
            q.append([nx, ny, 0, 1])
        elif [dx, dy] == [0, -1]:
            q.append([nx, ny, 1, 0])
    elif arr[nx][ny] == '2':
        if [dx, dy] == [1, 0]:
            q.append([nx, ny, 0, 1])
        elif [dx, dy] == [0, -1]:
            q.append([nx, ny, -1, 0])
    elif arr[nx][ny] == '3':
        if [dx, dy] == [1, 0]:
            q.append([nx, ny, 0, -1])
        elif [dx, dy] == [0, 1]:
            q.append([nx, ny, -1, 0])
    elif arr[nx][ny] == '4':
        if [dx, dy] == [-1, 0]:
            q.append([nx, ny, 0, -1])
        elif [dx, dy] == [0, 1]:
            q.append([nx, ny, 1, 0])
    elif arr[nx][ny] in ['|', '-', '+']:
        q.append([nx, ny, dx, dy])
    else:
        blank = [nx, ny]
check = []
for dx, dy in move:
    nx, ny = blank[0] + dx, blank[1] + dy
    if 0 <= nx < r and 0 <= ny < c:
        if [dx, dy] == [-1, 0] and (arr[nx][ny] in ['|', '+', '1', '4']):
            check.append([dx, dy])
        elif [dx, dy] == [1, 0] and (arr[nx][ny] in ['|', '+', '2', '3']):
            check.append([dx, dy])
        elif [dx, dy] == [0, -1] and (arr[nx][ny] in ['-', '+', '1', '2']):
            check.append([dx, dy])
        elif [dx, dy] == [0, 1] and (arr[nx][ny] in ['-', '+', '3', '4']):
            check.append([dx, dy])
pipe = ''
if check == [[-1, 0], [1, 0]]:
    pipe = '|'
elif check == [[0, -1], [0, 1]]:
    pipe = '-'
elif check == [[-1, 0], [1, 0], [0, -1], [0, 1]]:
    pipe = '+'
elif check == [[1, 0], [0, 1]]:
    pipe = '1'
elif check == [[-1, 0], [0, 1]]:
    pipe = '2'
elif check == [[-1, 0], [0, -1]]:
    pipe = '3'
elif check == [[1, 0], [0, -1]]:
    pipe = '4'
print(blank[0] + 1, blank[1] + 1, pipe)
