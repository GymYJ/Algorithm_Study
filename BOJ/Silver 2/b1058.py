import sys
from collections import deque

n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    arr.append(list(sys.stdin.readline().strip()))
answer = 0
for i in range(n):
    visit = [0] * n
    visit[i] = 1
    count = 0
    q = deque([[i, 0]])
    while q:
        now, c = q.popleft()
        if c == 2:
            continue
        for j in range(n):
            if arr[now][j] == 'Y' and visit[j] == 0:
                visit[j] = 1
                count += 1
                q.append([j, c + 1])
    if answer < count:
        answer = count
print(answer)

