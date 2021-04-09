import sys


def check():
    global n, h, bridge
    for start in range(1, n + 1):
        k = start
        for i in range(1, h + 1):
            if bridge[i][k] == 1:
                k += 1
            elif bridge[i][k - 1] == 1:
                k -= 1
        if start != k:
            return False
    return True


def bfs(cnt, x, y):
    global n, h, ans, bridge
    if check():
        ans = min(ans, cnt)
        return
    elif cnt == 3 or ans <= cnt:
        return

    for i in range(x, h + 1):
        if i == x:
            k = y
        else:
            k = 1
        for j in range(k, n):
            if bridge[i][j - 1] == 0 and bridge[i][j] == 0 and bridge[i][j + 1] == 0:
                bridge[i][j] = 1
                bfs(cnt + 1, i, j + 2)
                bridge[i][j] = 0


n, m, h = map(int, sys.stdin.readline().split())
if m == 0:
    print(0)
    sys.exit()
bridge = [[0 for _ in range(n + 1)] for _ in range(h + 1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    bridge[a][b] = 1
ans = 4
bfs(0, 1, 1)
print(ans if ans < 4 else -1)
