import sys
import heapq

m, n = map(int, sys.stdin.readline().split())
arr = [[0 for _ in range(m + 1)]]
for _ in range(n):
    arr.append([0] + list(map(int, list(sys.stdin.readline().strip()))))
check = [[10000 for _ in range(m + 1)] for _ in range(n + 1)]
check[n][m] = 0
move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
heap = []
heapq.heappush(heap, (0, n, m))
while heap:
    count, x, y = heapq.heappop(heap)
    if check[x][y] < count:
        continue
    if x == 1 and y == 1:
        print(count)
        break
    for dx, dy in move:
        nx, ny = x + dx, y + dy
        if 1 <= nx <= n and 1 <= ny <= m:
            if arr[nx][ny] == 1:
                if check[nx][ny] > count + 1:
                    heapq.heappush(heap, (count + 1, nx, ny))
                    check[nx][ny] = count + 1
            else:
                if check[nx][ny] > count:
                    heapq.heappush(heap, (count, nx, ny))
                    check[nx][ny] = count
