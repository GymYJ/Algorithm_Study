import sys

n, b = map(int, sys.stdin.readline().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))


def multiply(arr_, b_):
    if b_ == 1:
        return arr_
    half_b = b_ // 2
    half_arr = multiply(arr_, half_b)
    new_arr = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                new_arr[i][j] += half_arr[i][k] * half_arr[k][j]
            new_arr[i][j] %= 1000
    if b_ % 2 == 1:
        temp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    temp[i][j] += new_arr[i][k] * arr_[k][j]
                temp[i][j] %= 1000
        new_arr = temp
    return new_arr


arr = multiply(arr, b)
for i in range(n):
    for j in range(n):
        arr[i][j] = arr[i][j] % 1000
for a in arr:
    print(' '.join(list(map(str, a))))
