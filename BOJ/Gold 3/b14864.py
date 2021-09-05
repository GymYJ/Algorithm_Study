import sys

n, m = map(int, sys.stdin.readline().split())
arr = [i for i in range(n + 1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    arr[a] += 1
    arr[b] -= 1
visit = [0 for _ in range(n + 1)]
for num in arr[1:]:
    if num > n or num <= 0 or visit[num] == 1:
        print(-1)
        sys.exit()
    visit[num] = 1
print(*arr[1:])
