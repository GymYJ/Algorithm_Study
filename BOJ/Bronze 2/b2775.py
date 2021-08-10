import sys

t = int(sys.stdin.readline())
arr = [[i for i in range(15)] for _ in range(15)]
for i in range(1, 15):
    people = 0
    for j in range(1, 15):
        people += arr[i - 1][j]
        arr[i][j] = people
for _ in range(t):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    print(arr[k][n])
