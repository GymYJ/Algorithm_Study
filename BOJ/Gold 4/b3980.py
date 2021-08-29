import sys


def dfs(idx, power):
    global players, answer, pick
    if idx == 11:
        if answer < power:
            answer = power
        return
    for i, pos in enumerate(players[idx]):
        if pick[i] == 0 and pos > 0:
            pick[i] = 1
            dfs(idx + 1, power + pos)
            pick[i] = 0


c = int(sys.stdin.readline())
for _ in range(c):
    players = []
    for _ in range(11):
        players.append(list(map(int, sys.stdin.readline().split())))
    answer = 0
    pick = [0 for _ in range(11)]
    dfs(0, 0)
    print(answer)
