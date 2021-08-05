import sys

n = int(sys.stdin.readline())
before = []
flower = []
for _ in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    start, end = temp[:2], temp[2:]
    if start <= [3, 1]:
        before.append([start, end])
    else:
        flower.append([start, end])
flower.sort()
answer = 0
now = [[0, 0], [3, 1]]
for f in before:
    if now[1] < f[1]:
        now = f
        answer = 1
if answer == 0:
    print(0)
    sys.exit()
if now[1] > [11, 30]:
    print(answer)
    sys.exit()
idx = 0
while idx < len(flower):
    best = now.copy()
    is_p = False
    while idx < len(flower) and flower[idx][0] <= now[1]:
        if best[1] < flower[idx][1]:
            best = flower[idx]
            is_p = True
        idx += 1
    if not is_p:
        print(0)
        sys.exit()
    else:
        now = best
        answer += 1
    if now[1] > [11, 30]:
        break
if now[1] > [11, 30]:
    print(answer)
else:
    print(0)
