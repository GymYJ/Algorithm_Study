import sys
from collections import deque

r, c = map(int, sys.stdin.readline().split())
arr = []
now = ()
water = []
for i in range(r):
    temp = list(sys.stdin.readline().strip())
    if 'S' in temp:
        now = (i, temp.index('S'))
    for j in range(c):
        if temp[j] == '*':
            water.append((i, j))
    arr.append(temp)
sq = deque([now])
wq = deque(water)
safe = False
time = 0
move = [(-1, 0), (0, 1), (1, 0), (0, -1)]
visit = [now]
while True:
    time += 1
    wt = []
    while wq:
        x, y = wq.popleft()
        for dx, dy in move:
            nx, ny = x + dx, y + dy
            if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] in ['.', 'S']:
                wt.append((nx, ny))
                arr[nx][ny] = '*'
    wq = deque(wt)
    st = []
    while sq:
        x, y = sq.popleft()
        for dx, dy in move:
            nx, ny = x + dx, y + dy
            if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] not in ['*', 'X'] and (nx, ny) not in visit:
                if arr[nx][ny] == 'D':
                    safe = True
                    break
                st.append((nx, ny))
                visit.append((nx, ny))
        if safe:
            break
    if safe:
        break
    if len(st) == 0:
        break
    sq = deque(st)
if safe:
    print(time)
else:
    print('KAKTUS')
