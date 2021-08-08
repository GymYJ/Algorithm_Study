import sys

n = int(sys.stdin.readline())
answer = 0
for i in range(1, 1000000):
    if i >= n:
        break
    total = i
    temp = i
    for j in range(6, -1, -1):
        total += temp // (10 ** j)
        temp = i % (10 ** j)
    if total == n:
        answer = i
        break
print(answer)
