import sys


def calc(a, b, cal):
    if cal == '+':
        return a + b
    elif cal == '-':
        return a - b
    else:
        return a * b


def dfs(value, idx):
    global answer, ex, n
    if idx > n:
        if answer < value:
            answer = value
        return
    for i in range(idx, n, 2):
        if i < n - 2:
            temp = calc(int(ex[i]), int(ex[i + 2]), ex[i + 1])
            temp = calc(value, temp, ex[i - 1])
            dfs(temp, i + 4)
            value = calc(value, int(ex[i]), ex[i - 1])
        if i == n - 1:
            temp = calc(value, int(ex[i]), ex[i - 1])
            dfs(temp, i + 2)


n = int(sys.stdin.readline())
ex = sys.stdin.readline().strip()
if n == 1:
    print(int(ex))
elif n == 3:
    print(calc(int(ex[0]), int(ex[2]), ex[1]))
else:
    answer = -sys.maxsize
    dfs(int(ex[0]), 2)
    print(answer)
