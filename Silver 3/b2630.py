n = int(input())
paper = []
for _ in range(n):
    row = input().split()
    paper.append(row)
zero = 0
one = 0


def cut(x, y, size):
    global paper
    global zero
    global one
    init = paper[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper[i][j] != init:
                size = size // 2
                cut(x, y, size)
                cut(x + size, y, size)
                cut(x, y + size, size)
                cut(x + size, y + size, size)
                return
    if init == '0':
        zero += 1
    else:
        one += 1


cut(0, 0, n)
print(zero)
print(one)
