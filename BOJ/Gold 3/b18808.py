import sys


def spin(arr_):
    temp_ = []
    for a, b in arr_:
        temp_.append([b, -a])
    temp_.sort()
    bx, by = temp_[0]
    for t in temp_:
        t[0] -= bx
        t[1] -= by
    return temp_


def attach(sticker_):
    global arr, answer
    for a in range(n):
        for b in range(m):
            if arr[a][b] == 0:
                visit = []
                is_p = True
                for x, y in sticker_:
                    nx, ny = x + a, y + b
                    if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0:
                        visit.append([nx, ny])
                        continue
                    else:
                        is_p = False
                        break
                if is_p:
                    for x, y in visit:
                        arr[x][y] = 1
                        answer += 1
                    return True
    return False


n, m, k = map(int, sys.stdin.readline().split())
stickers = []
for _ in range(k):
    r, c = map(int, sys.stdin.readline().split())
    sticker = []
    for _ in range(r):
        sticker.append(list(map(int, sys.stdin.readline().split())))
    temp = []
    for i in range(r):
        for j in range(c):
            if sticker[i][j] == 1:
                temp.append([i, j])
    temp.sort()
    bx, by = temp[0]
    for t in temp:
        t[0] -= bx
        t[1] -= by
    stickers.append(temp)
arr = [[0 for _ in range(m)] for _ in range(n)]
answer = 0
for sticker in stickers:
    for _ in range(4):
        if attach(sticker):
            break
        sticker = spin(sticker)
print(answer)
