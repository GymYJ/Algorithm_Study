import sys
from math import inf

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
arr = [[inf for _ in range(n + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    arr[i][i] = 1

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    arr[a][b] = 1
    arr[b][a] = 1

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])

check = [0 for _ in range(n + 1)]
answer = []
for i in range(1, n + 1):
    if check[i] == 0:
        nums = []
        for j in range(1, n + 1):
            if arr[i][j] != inf:
                check[j] = 1
                nums.append(j)
        min_value = inf
        represent = 0
        for j in nums:
            temp = set(arr[j])
            temp.remove(inf)
            if min_value > max(temp):
                min_value = max(temp)
                represent = j
        answer.append(represent)
answer.sort()
print(len(answer))
for i in answer:
    print(i)
