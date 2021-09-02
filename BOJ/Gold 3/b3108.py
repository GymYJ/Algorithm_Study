import sys

n = int(sys.stdin.readline())
visit = [[0 for _ in range(1001)] for _ in range(1001)]
rank = {}
rank_list = {}
for j in range(1, n + 1):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    x1, y1, x2, y2 = x1 + 500, y1 + 500, x2 + 500, y2 + 500
    rank[j] = j
    rank_list[j] = [j]
    check = False
    combine = []
    if x1 > x2:
        temp = x1
        x1 = x2
        x2 = temp
    if y1 > y2:
        temp = y1
        y1 = y2
        y2 = temp
    for i in range(x1, x2 + 1):
        if visit[i][y1] != 0:
            check = True
            combine.append(rank[visit[i][y1]])
        visit[i][y1] = j
        if visit[i][y2] != 0:
            check = True
            combine.append(rank[visit[i][y2]])
        visit[i][y2] = j
    for i in range(y1, y2 + 1):
        if visit[x1][i] != 0:
            check = True
            combine.append(rank[visit[x1][i]])
        visit[x1][i] = j
        if visit[x2][i] != 0:
            check = True
            combine.append(rank[visit[x2][i]])
        visit[x2][i] = j
    if check:
        basis = rank[list(set(combine)).pop()]
        combine.append(j)
        renew = []
        for i in combine:
            renew += rank_list[i]
            rank_list[i] = []
        for i in renew:
            rank[i] = basis
        rank_list[basis] += renew
answer = len(set(rank.values()))
if visit[500][500] != 0:
    answer -= 1
print(answer)
