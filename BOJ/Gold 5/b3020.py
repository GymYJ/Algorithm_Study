import sys

n, h = map(int, sys.stdin.readline().split())
sun = [0] * (h + 1)
suk = [0] * (h + 1)
for _ in range(n // 2):
    sun[int(sys.stdin.readline())] += 1
    suk[int(sys.stdin.readline())] += 1
for i in range(h - 1, 0, -1):
    sun[i] += sun[i + 1]
    suk[i] += suk[i + 1]

answer = n
count = 0
for i in range(1, h + 1):
    if answer > sun[i] + suk[h - i + 1]:
        answer = sun[i] + suk[h - i + 1]
        count = 1
    elif answer == sun[i] + suk[h - i + 1]:
        count += 1

print(answer, count)
