import sys

n = int(sys.stdin.readline())
# 해당 열의 [깊이, 빠질 물의 깊이]
depth = [[0, 0] for _ in range(40001)]
a, b = map(int, sys.stdin.readline().split())
for i in range(n // 2 - 1):
    a, b = map(int, sys.stdin.readline().split())
    c, d = map(int, sys.stdin.readline().split())
    for j in range(a, c):
        depth[j][0] = b
a, b = map(int, sys.stdin.readline().split())
row = a

k = int(sys.stdin.readline())
hole = []
for _ in range(k):
    a, b, c, d = map(int, sys.stdin.readline().split())
    hole.append(a)
for i in hole:
    x = i
    height = depth[x][0]
    # 구멍
    depth[x][1] = height
    # 구멍으로부터 왼쪽
    for j in range(x - 1, -1, -1):
        height = min(height, depth[j][0])
        remove = max(depth[j][1], height)
        if remove <= depth[j][1]:
            break
        depth[j][1] = remove
    height = depth[x][0]
    # 구멍으로부터 오른쪽
    for j in range(x + 1, row):
        height = min(height, depth[j][0])
        remove = max(depth[j][1], height)
        if remove <= depth[j][1]:
            break
        depth[j][1] = remove

answer = 0
for i in range(0, row):
    answer += depth[i][0] - depth[i][1]
print(answer)
