import sys

n = int(sys.stdin.readline())
arr = []
last_day = 0
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    arr.append([b, a])
    last_day = max(last_day, b)
arr.sort()
answer = 0
pays = []
for day in range(last_day, 0, -1):
    while arr and arr[-1][0] == day:
        pays.append(arr.pop()[1])
    if pays:
        p = max(pays)
        answer += p
        pays.remove(p)
print(answer)
