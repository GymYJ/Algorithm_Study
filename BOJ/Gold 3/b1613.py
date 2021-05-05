import sys

n, k = map(int, sys.stdin.readline().split())
arr = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
for _ in range(k):
    a, b = map(int, sys.stdin.readline().split())
    arr[a][b] = -1
    arr[b][a] = 1

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if arr[i][j] == 0 and (arr[i][k] == -1 and arr[k][j] == -1):
                arr[i][j] = -1
            elif arr[i][j] == 0 and (arr[i][k] == 1 and arr[k][j] == 1):
                arr[i][j] = 1

s = int(sys.stdin.readline())
for _ in range(s):
    a, b = map(int, sys.stdin.readline().split())
    print(arr[a][b])
