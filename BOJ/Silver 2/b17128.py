import sys

n, q = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
swap = list(map(int, sys.stdin.readline().split()))
total = [0 for _ in range(n)]
for i in range(n - 1, -1, -1):
    total[i] = arr[i] * arr[i - 1] * arr[i - 2] * arr[i - 3]
answer = sum(total)
for i in swap:
    arr[i - 1] = arr[i - 1] * (-1)
    for j in range(i + 2, i - 2, -1):
        if j >= n:
            j = j - n
        answer -= total[j]
        total[j] = arr[j] * arr[j - 1] * arr[j - 2] * arr[j - 3]
        answer += total[j]
    print(answer)
