import sys


def comb(num):
    global gi
    parent = 1
    for i in range(num, num - 3, -1):
        parent *= i
    gi += parent // 6


n = int(sys.stdin.readline())
edge = []
degree = [0 for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    degree[a] += 1
    degree[b] += 1
    edge.append((a, b))

di = 0
gi = 0
for a, b in edge:
    di += (degree[a] - 1) * (degree[b] - 1)
for i in range(1, n + 1):
    if degree[i] >= 3:
        comb(degree[i])

if di > gi * 3:
    print('D')
elif di < gi * 3:
    print('G')
else:
    print('DUDUDUNGA')
