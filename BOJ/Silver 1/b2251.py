import sys


def dfs(aa, bb, cc):
    global answer, a, b, c
    if visit[aa][bb][cc] == 1:
        return
    visit[aa][bb][cc] = 1
    if aa == 0:
        answer.add(cc)
    if aa < a:
        if a - aa >= bb:
            dfs(aa + bb, 0, cc)
        else:
            dfs(a, bb - (a - aa), cc)
        if a - aa >= cc:
            dfs(aa + cc, bb, 0)
        else:
            dfs(a, bb, cc - (a - aa))
    if bb < b:
        if b - bb >= aa:
            dfs(0, aa + bb, cc)
        else:
            dfs(aa - (b - bb), b, cc)
        if b - bb >= cc:
            dfs(aa, bb + cc, 0)
        else:
            dfs(aa, b, cc - (b - bb))
    if cc < c:
        if c - cc >= aa:
            dfs(0, bb, aa + cc)
        else:
            dfs(aa - (c - cc), bb, c)
        if c - cc >= bb:
            dfs(aa, 0, bb + cc)
        else:
            dfs(aa, bb - (c - cc), c)


a, b, c = map(int, sys.stdin.readline().split())
visit = [[[0 for _ in range(c + 1)] for _ in range(b + 1)] for _ in range(a + 1)]
answer = set()
dfs(0, 0, c)
answer = list(answer)
answer.sort()
print(' '.join(map(str, answer)))
