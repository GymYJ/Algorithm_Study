import sys

n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))
check = [[1 for _ in range(n)] for _ in range(n)]
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j or j == k or i == k:
                continue
            if arr[i][j] == arr[i][k] + arr[k][j]:
                check[i][j] = 0
            elif arr[i][j] > arr[i][k] + arr[k][j]:
                print(-1)
                sys.exit()
answer = 0
for i in range(n):
    for j in range(i, n):
        if check[i][j]:
            answer += arr[i][j]
print(answer)
