import sys

n, m, x, y, k = map(int, sys.stdin.readline().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))
move = list(map(int, sys.stdin.readline().split()))
top, bottom, east, west, north, south = 0, 0, 0, 0, 0, 0
answer = []
for mv in move:
    if mv == 1:
        if y + 1 < m:
            y += 1
            temp = top
            top = west
            west = bottom
            bottom = east
            east = temp
        else:
            continue
    elif mv == 2:
        if y - 1 >= 0:
            y -= 1
            temp = top
            top = east
            east = bottom
            bottom = west
            west = temp
        else:
            continue
    elif mv == 3:
        if x - 1 >= 0:
            x -= 1
            temp = top
            top = south
            south = bottom
            bottom = north
            north = temp
        else:
            continue
    else:
        if x + 1 < n:
            x += 1
            temp = top
            top = north
            north = bottom
            bottom = south
            south = temp
        else:
            continue
    if arr[x][y] == 0:
        arr[x][y] = bottom
    else:
        bottom = arr[x][y]
        arr[x][y] = 0
    answer.append(top)
for a in answer:
    print(a)
