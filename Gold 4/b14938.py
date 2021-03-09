import sys

n, m, r = map(int, sys.stdin.readline().split())
item = [0] + list(map(int, sys.stdin.readline().split()))
inf = sys.maxsize
arr = [[inf for _ in range(n + 1)] for _ in range(n + 1)]
for _ in range(r):
    a, b, l = map(int, sys.stdin.readline().split())
    if arr[a][b] > l:
        arr[a][b] = l
    if arr[b][a] > l:
        arr[b][a] = l
for i in range(1, n + 1):
    arr[i][i] = 0

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])

answer = 0
for i in range(1, n + 1):
    temp = 0
    for j, leng in enumerate(arr[i]):
        if leng <= m:
            temp += item[j]
    if answer < temp:
        answer = temp
print(answer)
