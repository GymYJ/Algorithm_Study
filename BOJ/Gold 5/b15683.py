import sys
import copy
from itertools import product


def check(d, temp_arr):
    if d == 1:
        for j in range(x - 1, -1, -1):
            if temp_arr[j][y] == '0':
                temp_arr[j][y] = '#'
            if temp_arr[j][y] == '6':
                break
    elif d == 2:
        for j in range(y - 1, -1, -1):
            if temp_arr[x][j] == '0':
                temp_arr[x][j] = '#'
            if temp_arr[x][j] == '6':
                break
    elif d == 3:
        for j in range(x, n):
            if temp_arr[j][y] == '0':
                temp_arr[j][y] = '#'
            if temp_arr[j][y] == '6':
                break
    else:
        for j in range(y, m):
            if temp_arr[x][j] == '0':
                temp_arr[x][j] = '#'
            if temp_arr[x][j] == '6':
                break
    return temp_arr


n, m = map(int, sys.stdin.readline().split())
arr = []
cctv = []
answer = sys.maxsize
for i in range(n):
    temp = sys.stdin.readline().strip().split()
    for j in range(m):
        if temp[j] in ['1', '2', '3', '4', '5']:
            cctv.append((i, j))
    arr.append(temp)
for direction in product([1, 2, 3, 4], repeat=len(cctv)):
    temp_arr = copy.deepcopy(arr)
    for i, d in enumerate(direction):
        x, y = cctv[i]
        if arr[x][y] == '1':
            temp_arr = check(d, temp_arr)
        elif arr[x][y] == '2':
            if d in [1, 3]:
                temp_arr = check(1, temp_arr)
                temp_arr = check(3, temp_arr)
            else:
                temp_arr = check(2, temp_arr)
                temp_arr = check(4, temp_arr)
        elif arr[x][y] == '3':
            if d == 1:
                temp_arr = check(1, temp_arr)
                temp_arr = check(2, temp_arr)
            elif d == 2:
                temp_arr = check(2, temp_arr)
                temp_arr = check(3, temp_arr)
            elif d == 3:
                temp_arr = check(3, temp_arr)
                temp_arr = check(4, temp_arr)
            else:
                temp_arr = check(4, temp_arr)
                temp_arr = check(1, temp_arr)
        elif arr[x][y] == '4':
            if d == 1:
                temp_arr = check(1, temp_arr)
                temp_arr = check(2, temp_arr)
                temp_arr = check(3, temp_arr)
            elif d == 2:
                temp_arr = check(2, temp_arr)
                temp_arr = check(3, temp_arr)
                temp_arr = check(4, temp_arr)
            elif d == 3:
                temp_arr = check(3, temp_arr)
                temp_arr = check(4, temp_arr)
                temp_arr = check(1, temp_arr)
            else:
                temp_arr = check(4, temp_arr)
                temp_arr = check(1, temp_arr)
                temp_arr = check(2, temp_arr)
        elif arr[x][y] == '5':
            temp_arr = check(1, temp_arr)
            temp_arr = check(2, temp_arr)
            temp_arr = check(3, temp_arr)
            temp_arr = check(4, temp_arr)
    count = 0
    for temp in temp_arr:
        count += temp.count('0')
    if answer > count:
        answer = count
print(answer)
