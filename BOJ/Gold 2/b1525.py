import sys
from collections import deque


def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]
    return ''.join(arr)


start = ''
zero = []
for i in range(3):
    temp = sys.stdin.readline().split()
    start += ''.join(temp)
    for j in range(3):
        if temp[j] == '0':
            zero = [i, j]
visit = set()
visit.add(start)
move = [[-1, 0], [1, 0], [0, -1], [0, 1]]
q = deque([[start, zero[0], zero[1], 0]])
answer = -1
while q:
    now, x, y, count = q.popleft()
    if now == '123456780':
        answer = count
        break
    for dx, dy in move:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new = swap(list(now), nx * 3 + ny, x * 3 + y)
            if new not in visit:
                visit.add(new)
                q.append([new, nx, ny, count + 1])
print(answer)
