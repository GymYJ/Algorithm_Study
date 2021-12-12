import sys

n = int(sys.stdin.readline())
x, y, e = map(int, sys.stdin.readline().split())
rooms = []
for _ in range(n):
    rooms.append(list(map(int, sys.stdin.readline().split())))
answer = 0
for i in range(n):
    xi, yi, ei = rooms[i]
    speed = e - (abs(x - xi) + abs(y - yi))
    for j in range(n):
        xj, yj, ej = rooms[j]
        speed -= max(0, ej - (abs(xi - xj) + abs(yi - yj)))
        if speed <= 0:
            break
    answer = max(answer, speed)
print(answer if answer else 'IMPOSSIBLE')
