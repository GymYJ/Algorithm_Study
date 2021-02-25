import sys


def spread(r, c, cleaner, area):
    new_area = [[0 for _ in range(c)] for _ in range(r)]
    x_list = [-1, 1, 0, 0]
    y_list = [0, 0, -1, 1]
    for i in range(r):
        for j in range(c):
            if area[i][j] > 0:
                s_v = area[i][j] // 5
                count = 0
                for x, y in zip(x_list, y_list):
                    new_x, new_y = i + x, j + y
                    if 0 <= new_x < r and 0 <= new_y < c and area[new_x][new_y] != -1:
                        new_area[new_x][new_y] += s_v
                        count += 1
                new_area[i][j] += area[i][j] - (s_v * count)
    for x, y in cleaner:
        new_area[x][y] = -1
    return new_area


def clean(r, c, cleaner, area):
    x, y = cleaner[0]
    x -= 1
    while x > 0:
        area[x][y] = area[x - 1][y]
        x -= 1
    while y < c - 1:
        area[x][y] = area[x][y + 1]
        y += 1
    while x < cleaner[0][0]:
        area[x][y] = area[x + 1][y]
        x += 1
    while y > 1:
        area[x][y] = area[x][y - 1]
        y -= 1
    area[x][y] = 0
    x, y = cleaner[1]
    x += 1
    while x < r - 1:
        area[x][y] = area[x + 1][y]
        x += 1
    while y < c - 1:
        area[x][y] = area[x][y + 1]
        y += 1
    while x > cleaner[1][0]:
        area[x][y] = area[x - 1][y]
        x -= 1
    while y > 1:
        area[x][y] = area[x][y - 1]
        y -= 1
    area[x][y] = 0
    return area


def main():
    r, c, t = map(int, sys.stdin.readline().split())
    area = []
    cleaner = []
    for i in range(r):
        temp = list(map(int, sys.stdin.readline().split()))
        if -1 in temp:
            cleaner.append((i, 0))
        area.append(temp)
    for _ in range(t):
        area = spread(r, c, cleaner, area)
        area = clean(r, c, cleaner, area)
    answer = 2
    for a in area:
        answer += sum(a)
    print(answer)


if __name__ == '__main__':
    main()
