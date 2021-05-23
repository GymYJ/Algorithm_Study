import sys

n, c = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
arr = []
for _ in range(m):
    arr.append(list(map(int, sys.stdin.readline().split())))
arr.sort(key=lambda x: x[1])
space = [c for _ in range(n + 1)]
answer = 0
for i in range(m):
    temp = c
    for j in range(arr[i][0], arr[i][1]):
        temp = min(temp, space[j])
    temp = min(temp, arr[i][2])
    for j in range(arr[i][0], arr[i][1]):
        space[j] -= temp
    answer += temp
print(answer)
