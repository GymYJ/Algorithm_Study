import sys

arr = [[0 for _ in range(10)] for _ in range(10)]
arr2 = [[[] for _ in range(10)] for _ in range(10)]
for i in range(10):
    arr[0][i] = 1
    arr2[0][i].append(i)
for i in range(9):
    for j in range(10):
        for k in range(j + 1, 10):
            arr[i + 1][k] += arr[i][j]
            for num in arr2[i][j]:
                arr2[i + 1][k].append(k * (10 ** (i + 1)) + num)
n = int(sys.stdin.readline())
count = 0
answer = 0
find = False
for i in range(10):
    for j in range(10):
        count += arr[i][j]
        if count > n:
            answer = arr2[i][j][n - (count - arr[i][j])]
            find = True
            break
    if find:
        break
print(answer if find else -1)
