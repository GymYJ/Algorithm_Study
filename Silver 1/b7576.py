from collections import deque

m, n = input().split()
box = []
count = int(m) * int(n)
q = deque([])
for i in range(int(n)):
    row = input().split()
    temp = []
    for j, r in enumerate(row):
        temp.append(int(r))
        if int(r) == -1:
            count -= 1
        elif int(r) == 1:
            q.append((i, j))
            count -= 1
    box.append(temp)
day = 0
tomorrow = deque([])
change = False
while q:
    y, x = q.popleft()
    if y + 1 < int(n) and box[y + 1][x] == 0:
        box[y + 1][x] = 1
        tomorrow.append((y + 1, x))
        count -= 1
        change = True
    if y - 1 >= 0 and box[y - 1][x] == 0:
        box[y - 1][x] = 1
        tomorrow.append((y - 1, x))
        count -= 1
        change = True
    if x + 1 < int(m) and box[y][x + 1] == 0:
        box[y][x + 1] = 1
        tomorrow.append((y, x + 1))
        count -= 1
        change = True
    if x - 1 >= 0 and box[y][x - 1] == 0:
        box[y][x - 1] = 1
        tomorrow.append((y, x - 1))
        count -= 1
        change = True
    if len(q) == 0:
        if change:
            day += 1
        q = tomorrow
        tomorrow = deque([])
        change = False


if count != 0:
    print(-1)
else:
    print(day)
