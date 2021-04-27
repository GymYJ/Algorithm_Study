import sys


def bt(row):
    global arr
    for i in range(row, 9):
        for j in range(9):
            if arr[i][j] == 0:
                for k in range(1, 10):
                    if isPossible(k, i, j):
                        arr[i][j] = k
                        if j == 8:
                            row += 1
                        if bt(row):
                            return True
                arr[i][j] = 0
                return False
    return True


def isPossible(num, row, col):
    global arr
    for i in range(9):
        if arr[row][i] == num or arr[i][col] == num:
            return False
    for i in range(row // 3 * 3, row // 3 * 3 + 3):
        for j in range(col // 3 * 3, col // 3 * 3 + 3):
            if arr[i][j] == num:
                return False
    return True


arr = []
for _ in range(9):
    arr.append(list(map(int, list(sys.stdin.readline().strip()))))
bt(0)
for a in arr:
    print(''.join(list(map(str, a))))
