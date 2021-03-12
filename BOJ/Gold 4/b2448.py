import sys

n = int(sys.stdin.readline())
star = [[' ' for _ in range(n * 2)] for _ in range(n)]


def draw(index, bottom, s):
    for i in range(s // 3):
        for j in range(5):
            star[bottom - 1][index + i * 6 + j] = '*'
    for i in range(s, 0, -1):
        star[bottom - i][index + i - 1] = '*'
    for i in range(s, 0, -1):
        star[bottom - i][index + s * 2 - i - 1] = '*'

    if s != 3:
        draw(index, bottom, s // 2)
        draw(index + s // 2, bottom - s // 2, s // 2)
        draw(index + s, bottom, s // 2)


draw(0, n, n)

for a in star:
    print(''.join(a))
