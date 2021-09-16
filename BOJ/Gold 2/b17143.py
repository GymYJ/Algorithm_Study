import sys

R, C, M = map(int, sys.stdin.readline().split())
move = [[0, 0], [-1, 0], [1, 0], [0, 1], [0, -1]]
col = [[] for _ in range(C + 1)]
for _ in range(M):
    r, c, s, d, z = map(int, sys.stdin.readline().split())
    col[c].append([r, c, s, z, move[d][0], move[d][1]])
answer = 0
for i in range(1, C + 1):
    sharks_to_move = []
    for j in range(1, i):
        sharks_to_move += col[j]
    col[i].sort()
    if col[i]:
        answer += col[i][0][3]
        for shark in col[i][1:]:
            sharks_to_move.append(shark)
    for j in range(i + 1, C + 1):
        sharks_to_move += col[j]
    loc = {}
    for r, c, s, z, x, y in sharks_to_move:
        for _ in range(s):
            if 1 <= r + x <= R and 1 <= c + y <= C:
                r = r + x
                c = c + y
            else:
                x, y = x * (-1), y * (-1)
                r = r + x
                c = c + y
        if loc.get((r, c)):
            if loc[(r, c)][3] < z:
                loc[(r, c)] = [r, c, s, z, x, y]
        else:
            loc[(r, c)] = [r, c, s, z, x, y]
    col = [[] for _ in range(C + 1)]
    for key in loc:
        r, c, s, z, x, y = loc[key]
        col[c].append([r, c, s, z, x, y])
print(answer)
